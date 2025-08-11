#!/usr/bin/env python3
"""
Sandbox script for testing the Mosaia Python SDK.

This script provides a testing environment for the Mosaia Python SDK,
similar to the Node.js sandbox.ts file. It demonstrates authentication,
API operations, and basic SDK functionality.

Usage:
    python sandbox.py

Environment Variables Required:
    - API_URL: Base URL for the Mosaia API
    - CLIENT_ID: OAuth client ID
    - USER_EMAIL: User email for authentication
    - USER_PASSWORD: User password for authentication

The script will automatically load environment variables from a .env file
if python-dotenv is installed, or you can set them manually.

Example .env file:
    API_URL=https://api.mosaia.ai
    CLIENT_ID=your-client-id
    USER_EMAIL=user@example.com
    USER_PASSWORD=your-password

Example manual setup:
    export API_URL="https://api.mosaia.ai"
    export CLIENT_ID="your-client-id"
    export USER_EMAIL="user@example.com"
    export USER_PASSWORD="your-password"
    python sandbox.py
"""

import asyncio
import logging
import os
import sys
from typing import Optional

# Add the current directory to the path for local development
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configure logging so INFO logs from the SDK are visible
logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.getLogger("mosaia.utils.api_client").setLevel(logging.INFO)

# Try to load python-dotenv
try:
    from dotenv import load_dotenv
    # Load environment variables from .env file
    load_dotenv()
    print("✅ Loaded environment variables from .env file")
except ImportError:
    print("ℹ️  python-dotenv not found. Using system environment variables.")
    print("   Install with: pip install python-dotenv")

try:
    from mosaia import MosaiaClient, MosaiaConfig
    from mosaia.types import SessionInterface
except ImportError:
    print("❌ Mosaia SDK not found. Please install it first:")
    print("   pip install -e .")
    sys.exit(1)


def validate_environment() -> tuple[str, str, str, str]:
    """
    Validate that all required environment variables are set.
    
    Returns:
        Tuple of (api_url, client_id, user_email, user_password)
        
    Raises:
        SystemExit: If any required environment variables are missing
    """
    api_url = os.getenv('API_URL')
    client_id = os.getenv('CLIENT_ID')
    user_email = os.getenv('USER_EMAIL')
    user_password = os.getenv('USER_PASSWORD')
    
    if not all([api_url, client_id, user_email, user_password]):
        print('❌ Missing required environment variables:')
        print(f'   API_URL: {api_url or "[MISSING]"}')
        print(f'   CLIENT_ID: {client_id or "[MISSING]"}')
        print(f'   USER_EMAIL: {user_email or "[MISSING]"}')
        print(f'   USER_PASSWORD: {"[SET]" if user_password else "[MISSING]"}')
        print()
        print('Please set these environment variables before running the sandbox:')
        print()
        print('Option 1: Create a .env file in the project root:')
        print('   API_URL=https://api.mosaia.ai')
        print('   CLIENT_ID=your-client-id')
        print('   USER_EMAIL=user@example.com')
        print('   USER_PASSWORD=your-password')
        print()
        print('Option 2: Set environment variables manually:')
        print('   export API_URL="https://api.mosaia.ai"')
        print('   export CLIENT_ID="your-client-id"')
        print('   export USER_EMAIL="user@example.com"')
        print('   export USER_PASSWORD="your-password"')
        print()
        print('Note: Install python-dotenv for automatic .env file loading:')
        print('   pip install python-dotenv')
        sys.exit(1)
    
    return api_url, client_id, user_email, user_password


async def authenticate(api_url: str, client_id: str, user_email: str, user_password: str) -> MosaiaClient:
    """
    Authenticate with the Mosaia API using email and password.
    
    Args:
        api_url: Base URL for the API
        client_id: OAuth client ID
        user_email: User email
        user_password: User password
        
    Returns:
        Authenticated MosaiaClient instance
        
    Raises:
        Exception: If authentication fails
    """
    try:
        print('🚀 Initializing Mosaia SDK...')
        
        # Create initial configuration using the dataclass
        initial_config = MosaiaConfig(
            api_url=api_url,
            client_id=client_id,
            version='1'
            # verbose=True
        )
        
        mosaia = MosaiaClient(initial_config)
        
        print('   Attempting to sign in...')
        auth_config = await mosaia.auth.sign_in_with_password(user_email, user_password)
        
        # Update the client with the authenticated configuration
        mosaia.config = auth_config
        
        print('✅ Authentication successful!')
        
        # Get and display session information
        try:
            session = await mosaia.session()
            if session and hasattr(session, 'user') and session.user:
                print(f'   Session user: {session.user.name or session.user.email or "N/A"}')
            if session and hasattr(session, 'org') and session.org:
                print(f'   Session org: {session.org.name or "N/A"}')
        except Exception as session_error:
            print(f'   Could not retrieve session info: {session_error}')
        
        return mosaia
        
    except Exception as error:
        print(f'❌ Error during authentication: {error}')
        if hasattr(error, 'message'):
            print(f'   Error message: {error.message}')
        raise


async def test_agents(mosaia: MosaiaClient) -> None:
    """
    Test agent-related functionality.
    
    Args:
        mosaia: Authenticated MosaiaClient instance
    """
    try:
        print('\n🔍 Testing agents functionality...')
        
        # Get agents with search query
        agents_response = await mosaia.agents.get({'q': 'cafe'})
        
        if not agents_response:
            print('   No agents found')
            return
        
        data = agents_response.data
        paging = agents_response.paging
        
        # # Handle different response formats
        # if isinstance(agents_response, dict):
        #     data = agents_response.get('data', [])
        #     paging = agents_response.get('paging')
        
        print(f'   Found {len(data) if isinstance(data, list) else 0} agents')
        if paging:
            print(f'   Paging: {paging}')
        
        if isinstance(data, list) and len(data) > 0:
            first_agent = data[0]
            print(f'   First agent: {first_agent.name}')
            print(f'   Description: {first_agent.description}')
            
            # Test chat completion with the first agent
            try:
                print('   Testing chat completion...')

                chat_completion_request = {
                    'messages': [
                        {
                            'role': 'user',
                            'content': 'Hello, who are you?'
                        }
                    ]
                }
                
                # Get the agent's chat completions
                response = await first_agent.chat.completions.create(chat_completion_request)
                    
                print(f'   Response: {response}')
                if response.choices:
                    message = response.choices[0]['message']
                    content = message.get('content', 'No response')
                    print(f'   Agent response: {content}')
                else:
                    print('   No response from agent')
                    
            except Exception as error:
                print(f'   ❌ Error testing chat completion: {error}')
                if hasattr(error, 'message'):
                    print(f'      Error message: {error.message}')
        
    except Exception as error:
        print(f'❌ Error testing agents: {error}')
        if hasattr(error, 'message'):
            print(f'   Error message: {error.message}')


async def test_users(mosaia: MosaiaClient) -> None:
    """
    Test user-related functionality.
    
    Args:
        mosaia: Authenticated MosaiaClient instance
    """
    try:
        print('\n👥 Testing users functionality...')
        
        # Get current user from session
        session = await mosaia.session()
        if session and hasattr(session, 'user') and session.user:
            user_name = session.user.name or session.user.email or "Unknown"
            user_email = session.user.email or "N/A"
            print(f'   Current user: {user_name} ({user_email})')
            
            # Test user's agents
            if hasattr(session.user, 'agents'):
                try:
                    user_agents = await session.user.agents.get()
                    data = user_agents.data
                    paging = user_agents.paging

                    print(f'   User agents: {data[0].name}')
                    print(f'   User agents paging: {paging}')
                except Exception as error:
                    print(f'   Could not fetch user agents: {error}')
            
            # Test user's organizations
            if hasattr(session.user, 'orgs'):
                try:
                    print(f'   User orgs: {session.user.orgs.uri}')
                    user_orgs = await session.user.orgs.get()

                    data = user_orgs.data
                    paging = user_orgs.paging

                    for org_user in data:
                        if org_user.org:
                            print(f'   Org user: {org_user.id}')
                            print(f'   Org user org: {org_user.org.name}')
                            print(f'   Org user org id: {org_user.org.id}')

                    # print(f'   User orgs: {data}')
                    print(f'   User orgs paging: {paging}')

                    org_user = await session.user.orgs.get({}, '65a9a716660e8cf0600b5095')
                    print(f'   SUPER USER ================================')
                    print(f'   Org user: {org_user}')
                    print(f'   Org user: {org_user.id}')
                    print(f'   Org user org: {org_user.org.name}')
                    print(f'   Org user org id: {org_user.org.id}')

                    org_user_config = await org_user.session()
                    print(f'   Org user config: {org_user_config}')

                    return MosaiaClient(org_user_config)
                except Exception as error:
                    print(f'   Could not fetch user organizations: {error}')
        
    except Exception as error:
        print(f'❌ Error testing users: {error}')
        if hasattr(error, 'message'):
            print(f'   Error message: {error.message}')


async def test_organizations(mosaia: MosaiaClient) -> None:
    """
    Test organization-related functionality.
    
    Args:
        mosaia: Authenticated MosaiaClient instance
    """
    try:
        print('\n🏢 Testing organizations functionality...')
        # Get organizations
        orgs_response = await mosaia.organizations.get()
        print(f'   Org response: {orgs_response}')

        if orgs_response:
            if isinstance(orgs_response, dict):
                data = orgs_response.get('data', [])
            else:
                data = orgs_response if isinstance(orgs_response, list) else []
            
            print(f'   Found {len(data) if isinstance(data, list) else 0} organizations')
            
            if isinstance(data, list) and len(data) > 0:
                first_org = data[0]
                print(f'   First organization: {first_org.get("name", "N/A")}')
                print(f'   Description: {first_org.get("short_description", "N/A")}')
        
    except Exception as error:
        print(f'❌ Error testing organizations: {error}')
        if hasattr(error, 'message'):
            print(f'   Error message: {error.message}')


async def test_tools(mosaia: MosaiaClient) -> None:
    """
    Test tools functionality.
    
    Args:
        mosaia: Authenticated MosaiaClient instance
    """
    try:
        print('\n🛠️ Testing tools functionality...')
        
        # Get tools
        tools_response = await mosaia.tools.get()
        
        if tools_response:
            if isinstance(tools_response, dict):
                data = tools_response.get('data', [])
            else:
                data = tools_response if isinstance(tools_response, list) else []
            
            print(f'   Found {len(data) if isinstance(data, list) else 0} tools')
            
            if isinstance(data, list) and len(data) > 0:
                first_tool = data[0]
                print(f'   First tool: {first_tool.get("name", "N/A")}')
                print(f'   Description: {first_tool.get("short_description", "N/A")}')
        
    except Exception as error:
        print(f'❌ Error testing tools: {error}')
        if hasattr(error, 'message'):
            print(f'   Error message: {error.message}')


async def main() -> None:
    """
    Main function to run the sandbox tests.
    """
    print('🧪 Mosaia Python SDK Sandbox')
    print('=' * 40)
    
    try:
        # Validate environment variables
        api_url, client_id, user_email, user_password = validate_environment()
        
        # Authenticate
        mosaia = await authenticate(api_url, client_id, user_email, user_password)
        
        # Run tests
        # await test_agents(mosaia)
        mosaia = await test_users(mosaia)
        print(f'   mosaia: {mosaia}')
        await test_organizations(mosaia)
        await test_tools(mosaia)
        
        print('\n✅ Sandbox tests completed successfully!')
        
    except KeyboardInterrupt:
        print('\n\n⏹️ Sandbox interrupted by user')
    except Exception as error:
        print(f'\n❌ Sandbox failed: {error}')
        if hasattr(error, 'message'):
            print(f'   Error message: {error.message}')
        sys.exit(1)


if __name__ == '__main__':
    # Run the async main function
    asyncio.run(main())
