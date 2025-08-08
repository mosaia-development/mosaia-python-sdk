"""
Organization class for managing organizational entities.

This class represents an organization in the Mosaia platform. Organizations
are the top-level containers that group users, resources, and settings.
They provide isolation and management capabilities for teams and enterprises.

Features:
- Resource management (agents, apps, models)
- Team management
- Access control
- Billing and usage tracking
- Configuration management

Organizations provide:
- Multi-tenant isolation
- Resource sharing and access control
- Team collaboration
- Usage monitoring and billing
- Custom configurations

Available resources:
- AI Agents
- Applications
- Agent Groups
- Models
- Tools
- OAuth Clients
- Team Members
"""

from typing import Any, Dict, Optional

from .base import BaseModel


class Organization(BaseModel[Dict[str, Any]]):
    """
    Organization class for managing organizational entities.
    
    This class represents an organization in the Mosaia platform. Organizations
    are the top-level containers that group users, resources, and settings.
    They provide isolation and management capabilities for teams and enterprises.
    
    Features:
    - Resource management (agents, apps, models)
    - Team management
    - Access control
    - Billing and usage tracking
    - Configuration management
    
    Examples:
        Basic organization setup:
        >>> # Create a new organization
        >>> org = Organization({
        ...     'name': 'Acme Inc',
        ...     'short_description': 'Technology solutions provider',
        ...     'metadata': {
        ...         'industry': 'technology',
        ...         'size': 'enterprise'
        ...     }
        ... })
        >>> 
        >>> await org.save()
        
        Resource management:
        >>> # Access organization resources
        >>> agents = await org.agents.get()
        >>> apps = await org.apps.get()
        >>> models = await org.models.get()
        >>> 
        >>> # Create new resources
        >>> agent = await org.agents.create({
        ...     'name': 'Support Bot',
        ...     'model': 'gpt-4'
        ... })
        >>> 
        >>> app = await org.apps.create({
        ...     'name': 'Customer Portal',
        ...     'short_description': 'AI-powered support'
        ... })
        >>> 
        >>> # Manage team members
        >>> members = await org.orgs.get()
        >>> print(f'Team size: {len(members)}')
    """
    
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        """
        Create a new organization instance.
        
        Initializes an organization with the provided configuration data.
        Organizations are the primary containers for managing AI resources,
        team members, and settings.
        
        Args:
            data: Configuration data including:
                  - name: Organization name
                  - short_description: Brief description
                  - long_description: Detailed description
                  - metadata: Custom metadata object
            uri: Optional custom URI path for the organization endpoint. Defaults to '/org'
            
        Examples:
            Basic organization:
            >>> org = Organization({
            ...     'name': 'Tech Solutions',
            ...     'short_description': 'AI solutions provider'
            ... })
            
            Detailed configuration:
            >>> org = Organization({
            ...     'name': 'Enterprise AI',
            ...     'short_description': 'Enterprise AI solutions',
            ...     'long_description': 'Comprehensive AI solutions for enterprises',
            ...     'metadata': {
            ...         'industry': 'technology',
            ...         'size': 'enterprise',
            ...         'region': 'global',
            ...         'compliance': ['gdpr', 'hipaa'],
            ...         'features': ['agents', 'models', 'apps']
            ...     }
            ... }, '/enterprise/org')
        """
        super().__init__(data, uri or '/org')
    
    @property
    def agents(self):
        """
        Get the organization's AI agents.
        
        This property provides access to the organization's AI agents through
        the Agents collection. It enables management of all AI agents within
        the organization.
        
        Returns:
            Agents collection for managing AI agents
            
        Examples:
            List agents:
            >>> agents = await org.agents.get()
            >>> for agent in agents:
            ...     print(f'Agent: {agent.name}')
            
            Create agent:
            >>> agent = await org.agents.create({
            ...     'name': 'Customer Support',
            ...     'model': 'gpt-4',
            ...     'temperature': 0.7,
            ...     'system_prompt': 'You are a helpful support agent.'
            ... })
        """
        return self._get_collection('agents')
    
    @property
    def apps(self):
        """
        Get the organization's applications.
        
        This property provides access to the organization's applications through
        the Apps collection. It enables management of all applications within
        the organization.
        
        Returns:
            Apps collection for managing applications
            
        Examples:
            List applications:
            >>> apps = await org.apps.get()
            >>> for app in apps:
            ...     print(f'App: {app.name}')
            ...     print(f'URL: {app.external_app_url}')
            
            Create application:
            >>> app = await org.apps.create({
            ...     'name': 'Support Portal',
            ...     'short_description': 'AI-powered support portal',
            ...     'external_app_url': 'https://support.example.com',
            ...     'metadata': {
            ...         'type': 'customer-support',
            ...         'features': ['chat', 'knowledge-base']
            ...     }
            ... })
        """
        return self._get_collection('apps')
    
    @property
    def models(self):
        """
        Get the organization's AI models.
        
        This property provides access to the organization's AI models through
        the Models collection. It enables management of model configurations
        and customizations for the organization's AI capabilities.
        
        Returns:
            Models collection for managing AI models
            
        Examples:
            List models:
            >>> models = await org.models.get()
            >>> for model in models:
            ...     print(f'Model: {model.name}')
            ...     print(f'Provider: {model.provider}')
            ...     print(f'ID: {model.model_id}')
            
            Create custom model:
            >>> model = await org.models.create({
            ...     'name': 'Enhanced GPT-4',
            ...     'provider': 'openai',
            ...     'model_id': 'gpt-4',
            ...     'temperature': 0.7,
            ...     'max_tokens': 2000,
            ...     'metadata': {
            ...         'purpose': 'customer-support',
            ...         'training': 'fine-tuned',
            ...         'version': '1.0'
            ...     }
            ... })
        """
        return self._get_collection('models')
    
    @property
    def tools(self):
        """
        Get the organization's tools.
        
        This property provides access to the organization's tools through the
        Tools collection. It enables management of custom tools and integrations
        that extend agent capabilities.
        
        Returns:
            Tools collection for managing custom tools
            
        Examples:
            List tools:
            >>> tools = await org.tools.get()
            >>> for tool in tools:
            ...     print(f'Tool: {tool.name}')
            ...     print(f'Type: {tool.type}')
            
            Create custom tool:
            >>> tool = await org.tools.create({
            ...     'name': 'Weather API',
            ...     'type': 'api',
            ...     'description': 'Get weather forecasts',
            ...     'api_url': 'https://api.weather.com',
            ...     'api_key': 'your-api-key',
            ...     'metadata': {
            ...         'provider': 'weather-service',
            ...         'capabilities': ['current', 'forecast'],
            ...         'rate_limit': 1000
            ...     }
            ... })
        """
        return self._get_collection('tools')
    
    @property
    def orgs(self):
        """
        Get the organization's team members.
        
        This property provides access to the organization's user relationships
        through the OrgUsers collection. It enables management of team members,
        their roles, and permissions within the organization.
        
        Returns:
            OrgUsers collection for managing team members
            
        Examples:
            List team members:
            >>> members = await org.orgs.get()
            >>> for member in members:
            ...     print(f'Member: {member.user.name}')
            ...     print(f'Role: {member.permission}')
            
            Add team member:
            >>> member = await org.orgs.create({
            ...     'user': 'user-123',
            ...     'permission': 'member',
            ...     'metadata': {
            ...         'department': 'engineering',
            ...         'title': 'Senior Developer',
            ...         'start_date': '2024-01-01T00:00:00Z'
            ...     }
            ... })
            >>> 
            >>> # Create session for member
            >>> session = await member.session()
        """
        return self._get_collection('orgs')
    
    @property
    def users(self):
        """
        Get the organization's users.
        
        This property provides access to the organization's users through the
        Users collection. It enables management of all users within the
        organization.
        
        Returns:
            Users collection for managing users
            
        Examples:
            List users:
            >>> users = await org.users.get()
            >>> for user in users:
            ...     print(f'User: {user.name}')
            ...     print(f'Email: {user.email}')
            
            Create user:
            >>> user = await org.users.create({
            ...     'username': 'john_doe',
            ...     'name': 'John Doe',
            ...     'email': 'john@example.com',
            ...     'metadata': {
            ...         'department': 'engineering',
            ...         'title': 'Senior Developer'
            ...     }
            ... })
        """
        return self._get_collection('users')
    
    @property
    def clients(self):
        """
        Get the organization's OAuth clients.
        
        This property provides access to the organization's OAuth clients through
        the Clients collection. It enables management of authentication and
        authorization for external applications.
        
        Returns:
            Clients collection for managing OAuth clients
            
        Examples:
            List clients:
            >>> clients = await org.clients.get()
            >>> for client in clients:
            ...     print(f'Client: {client.name}')
            ...     print(f'ID: {client.client_id}')
            
            Create OAuth client:
            >>> client = await org.clients.create({
            ...     'name': 'Web Dashboard',
            ...     'redirect_uris': ['https://app.example.com/oauth/callback'],
            ...     'scopes': ['read:agents', 'write:apps'],
            ...     'metadata': {
            ...         'type': 'web-application',
            ...         'environment': 'production'
            ...     }
            ... })
            >>> 
            >>> print('Client credentials:')
            >>> print(f'ID: {client.client_id}')
            >>> print(f'Secret: {client.client_secret}')
        """
        return self._get_collection('clients')
    
    @property
    def groups(self):
        """
        Get the organization's agent groups.
        
        This property provides access to the organization's agent groups through
        the AgentGroups collection. It enables management of collaborative
        agent teams and specialized agent configurations.
        
        Returns:
            AgentGroups collection for managing agent groups
            
        Examples:
            List agent groups:
            >>> groups = await org.groups.get()
            >>> for group in groups:
            ...     print(f'Group: {group.name}')
            ...     print(f'Agents: {len(group.agents)}')
            
            Create specialized team:
            >>> support_team = await org.groups.create({
            ...     'name': 'Support Team',
            ...     'short_description': 'Customer support specialists',
            ...     'agents': ['billing-expert', 'tech-support', 'general-help'],
            ...     'metadata': {
            ...         'type': 'customer-support',
            ...         'specialties': ['billing', 'technical', 'general'],
            ...         'availability': '24/7'
            ...     }
            ... })
        """
        return self._get_collection('groups')
    
    def _get_collection(self, collection_name: str):
        """
        Get a collection instance for this organization.
        
        This is a placeholder method that would return the appropriate
        collection instance based on the collection name.
        
        Args:
            collection_name: Name of the collection to get
            
        Returns:
            Collection instance
        """
        # This would be implemented to return the actual collection
        # For now, we'll return a placeholder
        return type(f'{collection_name.capitalize()}Collection', (), {
            'get': lambda: [],
            'create': lambda data: data
        })()
    
    async def upload_profile_image(self, file) -> 'Organization':
        """
        Upload organization profile image.
        
        This method uploads a profile image or logo for the organization.
        The image will be used to represent the organization in the platform
        and in various UI elements.
        
        Args:
            file: Image file to upload (supports common formats)
            
        Returns:
            Updated organization instance
            
        Raises:
            Error: When upload fails
            Error: When file format is invalid
            Error: When network errors occur
            
        Examples:
            Basic upload:
            >>> with open('logo.png', 'rb') as f:
            ...     org = await org.upload_profile_image(f)
            ...     print('Logo uploaded successfully')
            
            Upload with validation:
            >>> async def update_org_logo(org, file):
            ...     try:
            ...         # Validate file
            ...         if not file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            ...             raise Exception('Invalid file type')
            ...         
            ...         # Upload and update
            ...         updated = await org.upload_profile_image(file)
            ...         print('Logo updated successfully')
            ...         print(f'Size: {file.size} bytes')
            ...         print(f'Type: {file.type}')
            ...         
            ...         return updated
            ...     except Exception as error:
            ...         print(f'Logo update failed: {error}')
            ...         raise error
        """
        try:
            # This would implement the actual file upload logic
            # For now, we'll return the organization instance
            return self
        except Exception as error:
            raise self._handle_error(error)
