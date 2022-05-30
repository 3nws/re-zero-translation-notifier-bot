"""
This type stub file was generated by pyright.
"""

from typing import Any, Callable, ClassVar, Coroutine, Dict, Generator, Generic, List, Optional, TYPE_CHECKING, Type, TypeVar, Union, overload
from ..enums import AppCommandType
from .models import Choice, ChoiceT
from .errors import AppCommandError
from ..message import Message
from ..user import User
from ..member import Member
from ..permissions import Permissions
from typing_extensions import Concatenate, ParamSpec
from ..interactions import Interaction
from ..abc import Snowflake

"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
if TYPE_CHECKING:
    ErrorFunc = Callable[[Interaction, AppCommandError], Coroutine[Any, Any, None]]
__all__ = ('Command', 'ContextMenu', 'Group', 'context_menu', 'command', 'describe', 'check', 'rename', 'choices', 'autocomplete', 'guilds', 'guild_only', 'default_permissions')
if TYPE_CHECKING:
    P = ParamSpec('P')
else:
    ...
T = TypeVar('T')
F = TypeVar('F', bound=Callable[..., Any])
GroupT = TypeVar('GroupT', bound='Binding')
Coro = Coroutine[Any, Any, T]
UnboundError = Callable[['Interaction', AppCommandError], Coro[Any]]
Error = Union[Callable[[GroupT, 'Interaction', AppCommandError], Coro[Any]], UnboundError,]
Check = Callable[['Interaction'], Union[bool, Coro[bool]]]
Binding = Union['Group', 'Cog']
if TYPE_CHECKING:
    CommandCallback = Union[Callable[Concatenate[GroupT, 'Interaction', P], Coro[T]], Callable[Concatenate['Interaction', P], Coro[T]],]
    ContextMenuCallback = Union[Callable[['Interaction', Member], Coro[Any]], Callable[['Interaction', User], Coro[Any]], Callable[['Interaction', Message], Coro[Any]], Callable[['Interaction', Union[Member, User]], Coro[Any]],]
    AutocompleteCallback = Union[Callable[[GroupT, 'Interaction', ChoiceT], Coro[List[Choice[ChoiceT]]]], Callable[['Interaction', ChoiceT], Coro[List[Choice[ChoiceT]]]],]
else:
    ...
CheckInputParameter = Union['Command[Any, ..., Any]', 'ContextMenu', CommandCallback, ContextMenuCallback]
THAI_COMBINING = ...
DEVANAGARI_COMBINING = ...
VALID_SLASH_COMMAND_NAME = ...
CAMEL_CASE_REGEX = ...
ARG_NAME_SUBREGEX = ...
ARG_DESCRIPTION_SUBREGEX = ...
ARG_TYPE_SUBREGEX = ...
GOOGLE_DOCSTRING_ARG_REGEX = ...
SPHINX_DOCSTRING_ARG_REGEX = ...
NUMPY_DOCSTRING_ARG_REGEX = ...
def validate_name(name: str) -> str:
    ...

def validate_context_menu_name(name: str) -> str:
    ...

class Command(Generic[GroupT, P, T]):
    """A class that implements an application command.

    These are usually not created manually, instead they are created using
    one of the following decorators:

    - :func:`~discord.app_commands.command`
    - :meth:`Group.command <discord.app_commands.Group.command>`
    - :meth:`CommandTree.command <discord.app_commands.CommandTree.command>`

    .. versionadded:: 2.0

    Attributes
    ------------
    name: :class:`str`
        The name of the application command.
    description: :class:`str`
        The description of the application command. This shows up in the UI to describe
        the application command.
    checks
        A list of predicates that take a :class:`~discord.Interaction` parameter
        to indicate whether the command callback should be executed. If an exception
        is necessary to be thrown to signal failure, then one inherited from
        :exc:`AppCommandError` should be used. If all the checks fail without
        propagating an exception, :exc:`CheckFailure` is raised.
    default_permissions: Optional[:class:`~discord.Permissions`]
        The default permissions that can execute this command on Discord. Note
        that server administrators can override this value in the client.
        Setting an empty permissions field will disallow anyone except server
        administrators from using the command in a guild.

        Due to a Discord limitation, this does not work on subcommands.
    guild_only: :class:`bool`
        Whether the command should only be usable in guild contexts.
        Defaults to ``False``.

        Due to a Discord limitation, this does not work on subcommands.
    nsfw: :class:`bool`
        Whether the command is NSFW and should only work in NSFW channels.
        Defaults to ``False``.

        Due to a Discord limitation, this does not work on subcommands.
    parent: Optional[:class:`Group`]
        The parent application command. ``None`` if there isn't one.
    """
    def __init__(self, *, name: str, description: str, callback: CommandCallback[GroupT, P, T], nsfw: bool = ..., parent: Optional[Group] = ..., guild_ids: Optional[List[int]] = ...) -> None:
        ...
    
    def __set_name__(self, owner: Type[Any], name: str) -> None:
        ...
    
    @property
    def callback(self) -> CommandCallback[GroupT, P, T]:
        """:ref:`coroutine <coroutine>`: The coroutine that is executed when the command is called."""
        ...
    
    def to_dict(self) -> Dict[str, Any]:
        ...
    
    @property
    def root_parent(self) -> Optional[Group]:
        """Optional[:class:`Group`]: The root parent of this command."""
        ...
    
    @property
    def qualified_name(self) -> str:
        """:class:`str`: Returns the fully qualified command name.

        The qualified name includes the parent name as well. For example,
        in a command like ``/foo bar`` the qualified name is ``foo bar``.
        """
        ...
    
    def error(self, coro: Error[GroupT]) -> Error[GroupT]:
        """A decorator that registers a coroutine as a local error handler.

        The local error handler is called whenever an exception is raised in the body
        of the command or during handling of the command. The error handler must take
        2 parameters, the interaction and the error.

        The error passed will be derived from :exc:`AppCommandError`.

        Parameters
        -----------
        coro: :ref:`coroutine <coroutine>`
            The coroutine to register as the local error handler.

        Raises
        -------
        TypeError
            The coroutine passed is not actually a coroutine.
        """
        ...
    
    def autocomplete(self, name: str) -> Callable[[AutocompleteCallback[GroupT, ChoiceT]], AutocompleteCallback[GroupT, ChoiceT]]:
        """A decorator that registers a coroutine as an autocomplete prompt for a parameter.

        The coroutine callback must have 2 parameters, the :class:`~discord.Interaction`,
        and the current value by the user (usually either a :class:`str`, :class:`int`, or :class:`float`,
        depending on the type of the parameter being marked as autocomplete).

        To get the values from other parameters that may be filled in, accessing
        :attr:`.Interaction.namespace` will give a :class:`Namespace` object with those
        values.

        Parent :func:`checks <check>` are ignored within an autocomplete. However, checks can be added
        to the autocomplete callback and the ones added will be called. If the checks fail for any reason
        then an empty list is sent as the interaction response.

        The coroutine decorator **must** return a list of :class:`~discord.app_commands.Choice` objects.
        Only up to 25 objects are supported.

        Example:

        .. code-block:: python3

            @app_commands.command()
            async def fruits(interaction: discord.Interaction, fruit: str):
                await interaction.response.send_message(f'Your favourite fruit seems to be {fruit}')

            @fruits.autocomplete('fruit')
            async def fruits_autocomplete(
                interaction: discord.Interaction,
                current: str,
            ) -> List[app_commands.Choice[str]]:
                fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
                return [
                    app_commands.Choice(name=fruit, value=fruit)
                    for fruit in fruits if current.lower() in fruit.lower()
                ]


        Parameters
        -----------
        name: :class:`str`
            The parameter name to register as autocomplete.

        Raises
        -------
        TypeError
            The coroutine passed is not actually a coroutine or
            the parameter is not found or of an invalid type.
        """
        ...
    
    def add_check(self, func: Check, /) -> None:
        """Adds a check to the command.

        This is the non-decorator interface to :func:`check`.

        Parameters
        -----------
        func
            The function that will be used as a check.
        """
        ...
    
    def remove_check(self, func: Check, /) -> None:
        """Removes a check from the command.

        This function is idempotent and will not raise an exception
        if the function is not in the command's checks.

        Parameters
        -----------
        func
            The function to remove from the checks.
        """
        ...
    


class ContextMenu:
    """A class that implements a context menu application command.

    These are usually not created manually, instead they are created using
    one of the following decorators:

    - :func:`~discord.app_commands.context_menu`
    - :meth:`CommandTree.command <discord.app_commands.CommandTree.context_menu>`

    .. versionadded:: 2.0

    Attributes
    ------------
    name: :class:`str`
        The name of the context menu.
    type: :class:`.AppCommandType`
        The type of context menu application command. By default, this is inferred
        by the parameter of the callback.
    default_permissions: Optional[:class:`~discord.Permissions`]
        The default permissions that can execute this command on Discord. Note
        that server administrators can override this value in the client.
        Setting an empty permissions field will disallow anyone except server
        administrators from using the command in a guild.
    guild_only: :class:`bool`
        Whether the command should only be usable in guild contexts.
        Defaults to ``False``.
    nsfw: :class:`bool`
        Whether the command is NSFW and should only work in NSFW channels.
        Defaults to ``False``.
    checks
        A list of predicates that take a :class:`~discord.Interaction` parameter
        to indicate whether the command callback should be executed. If an exception
        is necessary to be thrown to signal failure, then one inherited from
        :exc:`AppCommandError` should be used. If all the checks fail without
        propagating an exception, :exc:`CheckFailure` is raised.
    """
    def __init__(self, *, name: str, callback: ContextMenuCallback, type: AppCommandType = ..., nsfw: bool = ..., guild_ids: Optional[List[int]] = ...) -> None:
        ...
    
    @property
    def callback(self) -> ContextMenuCallback:
        """:ref:`coroutine <coroutine>`: The coroutine that is executed when the context menu is called."""
        ...
    
    @property
    def qualified_name(self) -> str:
        """:class:`str`: Returns the fully qualified command name."""
        ...
    
    def to_dict(self) -> Dict[str, Any]:
        ...
    
    def error(self, coro: UnboundError) -> UnboundError:
        """A decorator that registers a coroutine as a local error handler.

        The local error handler is called whenever an exception is raised in the body
        of the command or during handling of the command. The error handler must take
        2 parameters, the interaction and the error.

        The error passed will be derived from :exc:`AppCommandError`.

        Parameters
        -----------
        coro: :ref:`coroutine <coroutine>`
            The coroutine to register as the local error handler.

        Raises
        -------
        TypeError
            The coroutine passed is not actually a coroutine.
        """
        ...
    
    def add_check(self, func: Check, /) -> None:
        """Adds a check to the command.

        This is the non-decorator interface to :func:`check`.

        Parameters
        -----------
        func
            The function that will be used as a check.
        """
        ...
    
    def remove_check(self, func: Check, /) -> None:
        """Removes a check from the command.

        This function is idempotent and will not raise an exception
        if the function is not in the command's checks.

        Parameters
        -----------
        func
            The function to remove from the checks.
        """
        ...
    


class Group:
    """A class that implements an application command group.

    These are usually inherited rather than created manually.

    Decorators such as :func:`guild_only`, :func:`guilds`, and :func:`default_permissions`
    will apply to the group if used on top of a subclass. For example:

    .. code-block:: python3

        from discord import app_commands

        @app_commands.guild_only()
        class MyGroup(app_commands.Group):
            pass

    .. versionadded:: 2.0

    Attributes
    ------------
    name: :class:`str`
        The name of the group. If not given, it defaults to a lower-case
        kebab-case version of the class name.
    description: :class:`str`
        The description of the group. This shows up in the UI to describe
        the group. If not given, it defaults to the docstring of the
        class shortened to 100 characters.
    default_permissions: Optional[:class:`~discord.Permissions`]
        The default permissions that can execute this group on Discord. Note
        that server administrators can override this value in the client.
        Setting an empty permissions field will disallow anyone except server
        administrators from using the command in a guild.

        Due to a Discord limitation, this does not work on subcommands.
    guild_only: :class:`bool`
        Whether the group should only be usable in guild contexts.
        Defaults to ``False``.

        Due to a Discord limitation, this does not work on subcommands.
    nsfw: :class:`bool`
        Whether the command is NSFW and should only work in NSFW channels.
        Defaults to ``False``.

        Due to a Discord limitation, this does not work on subcommands.
    parent: Optional[:class:`Group`]
        The parent group. ``None`` if there isn't one.
    """
    __discord_app_commands_group_children__: ClassVar[List[Union[Command[Any, ..., Any], Group]]] = ...
    __discord_app_commands_skip_init_binding__: bool = ...
    __discord_app_commands_group_name__: str = ...
    __discord_app_commands_group_description__: str = ...
    __discord_app_commands_group_nsfw__: bool = ...
    __discord_app_commands_guild_only__: bool = ...
    __discord_app_commands_default_permissions__: Optional[Permissions] = ...
    __discord_app_commands_has_module__: bool = ...
    def __init_subclass__(cls, *, name: str = ..., description: str = ..., guild_only: bool = ..., nsfw: bool = ..., default_permissions: Optional[Permissions] = ...) -> None:
        ...
    
    def __init__(self, *, name: str = ..., description: str = ..., parent: Optional[Group] = ..., guild_ids: Optional[List[int]] = ..., guild_only: bool = ..., nsfw: bool = ..., default_permissions: Optional[Permissions] = ...) -> None:
        ...
    
    def __set_name__(self, owner: Type[Any], name: str) -> None:
        ...
    
    def to_dict(self) -> Dict[str, Any]:
        ...
    
    @property
    def root_parent(self) -> Optional[Group]:
        """Optional[:class:`Group`]: The parent of this group."""
        ...
    
    @property
    def qualified_name(self) -> str:
        """:class:`str`: Returns the fully qualified group name.

        The qualified name includes the parent name as well. For example,
        in a group like ``/foo bar`` the qualified name is ``foo bar``.
        """
        ...
    
    @property
    def commands(self) -> List[Union[Command[Any, ..., Any], Group]]:
        """List[Union[:class:`Command`, :class:`Group`]]: The commands that this group contains."""
        ...
    
    def walk_commands(self) -> Generator[Union[Command[Any, ..., Any], Group], None, None]:
        """An iterator that recursively walks through all commands that this group contains.

        Yields
        ---------
        Union[:class:`Command`, :class:`Group`]
            The commands in this group.
        """
        ...
    
    async def on_error(self, interaction: Interaction, error: AppCommandError) -> None:
        """|coro|

        A callback that is called when a child's command raises an :exc:`AppCommandError`.

        To get the command that failed, :attr:`discord.Interaction.command` should be used.

        The default implementation does nothing.

        Parameters
        -----------
        interaction: :class:`~discord.Interaction`
            The interaction that is being handled.
        error: :exc:`AppCommandError`
            The exception that was raised.
        """
        ...
    
    def error(self, coro: ErrorFunc) -> ErrorFunc:
        """A decorator that registers a coroutine as a local error handler.

        The local error handler is called whenever an exception is raised in a child command.
        The error handler must take 2 parameters, the interaction and the error.

        The error passed will be derived from :exc:`AppCommandError`.

        Parameters
        -----------
        coro: :ref:`coroutine <coroutine>`
            The coroutine to register as the local error handler.

        Raises
        -------
        TypeError
            The coroutine passed is not actually a coroutine, or is an invalid coroutine.
        """
        ...
    
    async def interaction_check(self, interaction: Interaction) -> bool:
        """|coro|

        A callback that is called when an interaction happens within the group
        that checks whether a command inside the group should be executed.

        This is useful to override if, for example, you want to ensure that the
        interaction author is a given user.

        The default implementation of this returns ``True``.

        .. note::

            If an exception occurs within the body then the check
            is considered a failure and error handlers such as
            :meth:`on_error` is called. See :exc:`AppCommandError`
            for more information.

        Parameters
        -----------
        interaction: :class:`~discord.Interaction`
            The interaction that occurred.

        Returns
        ---------
        :class:`bool`
            Whether the view children's callbacks should be called.
        """
        ...
    
    def add_command(self, command: Union[Command[Any, ..., Any], Group], /, *, override: bool = ...) -> None:
        """Adds a command or group to this group's internal list of commands.

        Parameters
        -----------
        command: Union[:class:`Command`, :class:`Group`]
            The command or group to add.
        override: :class:`bool`
            Whether to override a pre-existing command or group with the same name.
            If ``False`` then an exception is raised.

        Raises
        -------
        CommandAlreadyRegistered
            The command or group is already registered. Note that the :attr:`CommandAlreadyRegistered.guild_id`
            attribute will always be ``None`` in this case.
        ValueError
            There are too many commands already registered or the group is too
            deeply nested.
        TypeError
            The wrong command type was passed.
        """
        ...
    
    def remove_command(self, name: str, /) -> Optional[Union[Command[Any, ..., Any], Group]]:
        """Removes a command or group from the internal list of commands.

        Parameters
        -----------
        name: :class:`str`
            The name of the command or group to remove.

        Returns
        --------
        Optional[Union[:class:`~discord.app_commands.Command`, :class:`~discord.app_commands.Group`]]
            The command that was removed. If nothing was removed
            then ``None`` is returned instead.
        """
        ...
    
    def get_command(self, name: str, /) -> Optional[Union[Command[Any, ..., Any], Group]]:
        """Retrieves a command or group from its name.

        Parameters
        -----------
        name: :class:`str`
            The name of the command or group to retrieve.

        Returns
        --------
        Optional[Union[:class:`~discord.app_commands.Command`, :class:`~discord.app_commands.Group`]]
            The command or group that was retrieved. If nothing was found
            then ``None`` is returned instead.
        """
        ...
    
    def command(self, *, name: str = ..., description: str = ..., nsfw: bool = ...) -> Callable[[CommandCallback[GroupT, P, T]], Command[GroupT, P, T]]:
        """Creates an application command under this group.

        Parameters
        ------------
        name: :class:`str`
            The name of the application command. If not given, it defaults to a lower-case
            version of the callback name.
        description: :class:`str`
            The description of the application command. This shows up in the UI to describe
            the application command. If not given, it defaults to the first line of the docstring
            of the callback shortened to 100 characters.
        nsfw: :class:`bool`
            Whether the command is NSFW and should only work in NSFW channels. Defaults to ``False``.
        """
        ...
    


def command(*, name: str = ..., description: str = ..., nsfw: bool = ...) -> Callable[[CommandCallback[GroupT, P, T]], Command[GroupT, P, T]]:
    """Creates an application command from a regular function.

    Parameters
    ------------
    name: :class:`str`
        The name of the application command. If not given, it defaults to a lower-case
        version of the callback name.
    description: :class:`str`
        The description of the application command. This shows up in the UI to describe
        the application command. If not given, it defaults to the first line of the docstring
        of the callback shortened to 100 characters.
    nsfw: :class:`bool`
        Whether the command is NSFW and should only work in NSFW channels. Defaults to ``False``.

        Due to a Discord limitation, this does not work on subcommands.
    """
    ...

def context_menu(*, name: str = ..., nsfw: bool = ...) -> Callable[[ContextMenuCallback], ContextMenu]:
    """Creates an application command context menu from a regular function.

    This function must have a signature of :class:`~discord.Interaction` as its first parameter
    and taking either a :class:`~discord.Member`, :class:`~discord.User`, or :class:`~discord.Message`,
    or a :obj:`typing.Union` of ``Member`` and ``User`` as its second parameter.

    Examples
    ---------

    .. code-block:: python3

        @app_commands.context_menu()
        async def react(interaction: discord.Interaction, message: discord.Message):
            await interaction.response.send_message('Very cool message!', ephemeral=True)

        @app_commands.context_menu()
        async def ban(interaction: discord.Interaction, user: discord.Member):
            await interaction.response.send_message(f'Should I actually ban {user}...', ephemeral=True)

    Parameters
    ------------
    name: :class:`str`
        The name of the context menu command. If not given, it defaults to a title-case
        version of the callback name. Note that unlike regular slash commands this can
        have spaces and upper case characters in the name.
    nsfw: :class:`bool`
        Whether the command is NSFW and should only work in NSFW channels. Defaults to ``False``.

        Due to a Discord limitation, this does not work on subcommands.
    """
    ...

def describe(**parameters: str) -> Callable[[T], T]:
    r"""Describes the given parameters by their name using the key of the keyword argument
    as the name.

    Example:

    .. code-block:: python3

        @app_commands.command()
        @app_commands.describe(member='the member to ban')
        async def ban(interaction: discord.Interaction, member: discord.Member):
            await interaction.response.send_message(f'Banned {member}')

    Parameters
    -----------
    \*\*parameters
        The description of the parameters.

    Raises
    --------
    TypeError
        The parameter name is not found.
    """
    ...

def rename(**parameters: str) -> Callable[[T], T]:
    r"""Renames the given parameters by their name using the key of the keyword argument
    as the name.

    Example:

    .. code-block:: python3

        @app_commands.command()
        @app_commands.rename(the_member_to_ban='member')
        async def ban(interaction: discord.Interaction, the_member_to_ban: discord.Member):
            await interaction.response.send_message(f'Banned {the_member_to_ban}')

    Parameters
    -----------
    \*\*parameters
        The name of the parameters.

    Raises
    --------
    ValueError
        The parameter name is already used by another parameter.
    TypeError
        The parameter name is not found.
    """
    ...

def choices(**parameters: List[Choice[ChoiceT]]) -> Callable[[T], T]:
    r"""Instructs the given parameters by their name to use the given choices for their choices.

    Example:

    .. code-block:: python3

        @app_commands.command()
        @app_commands.describe(fruits='fruits to choose from')
        @app_commands.choices(fruits=[
            Choice(name='apple', value=1),
            Choice(name='banana', value=2),
            Choice(name='cherry', value=3),
        ])
        async def fruit(interaction: discord.Interaction, fruits: Choice[int]):
            await interaction.response.send_message(f'Your favourite fruit is {fruits.name}.')

    .. note::

        This is not the only way to provide choices to a command. There are two more ergonomic ways
        of doing this. The first one is to use a :obj:`typing.Literal` annotation:

        .. code-block:: python3

            @app_commands.command()
            @app_commands.describe(fruits='fruits to choose from')
            async def fruit(interaction: discord.Interaction, fruits: Literal['apple', 'banana', 'cherry']):
                await interaction.response.send_message(f'Your favourite fruit is {fruits}.')

        The second way is to use an :class:`enum.Enum`:

        .. code-block:: python3

            class Fruits(enum.Enum):
                apple = 1
                banana = 2
                cherry = 3

            @app_commands.command()
            @app_commands.describe(fruits='fruits to choose from')
            async def fruit(interaction: discord.Interaction, fruits: Fruits):
                await interaction.response.send_message(f'Your favourite fruit is {fruits}.')


    Parameters
    -----------
    \*\*parameters
        The choices of the parameters.

    Raises
    --------
    TypeError
        The parameter name is not found or the parameter type was incorrect.
    """
    ...

def autocomplete(**parameters: AutocompleteCallback[GroupT, ChoiceT]) -> Callable[[T], T]:
    r"""Associates the given parameters with the given autocomplete callback.

    Autocomplete is only supported on types that have :class:`str`, :class:`int`, or :class:`float`
    values.

    :func:`Checks <check>` are supported, however they must be attached to the autocomplete
    callback in order to work. Checks attached to the command are ignored when invoking the autocomplete
    callback.

    For more information, see the :meth:`Command.autocomplete` documentation.

    Example:

    .. code-block:: python3

            @app_commands.command()
            @app_commands.autocomplete(fruit=fruit_autocomplete)
            async def fruits(interaction: discord.Interaction, fruit: str):
                await interaction.response.send_message(f'Your favourite fruit seems to be {fruit}')

            async def fruit_autocomplete(
                interaction: discord.Interaction,
                current: str,
            ) -> List[app_commands.Choice[str]]:
                fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
                return [
                    app_commands.Choice(name=fruit, value=fruit)
                    for fruit in fruits if current.lower() in fruit.lower()
                ]

    Parameters
    -----------
    \*\*parameters
        The parameters to mark as autocomplete.

    Raises
    --------
    TypeError
        The parameter name is not found or the parameter type was incorrect.
    """
    ...

def guilds(*guild_ids: Union[Snowflake, int]) -> Callable[[T], T]:
    r"""Associates the given guilds with the command.

    When the command instance is added to a :class:`CommandTree`, the guilds that are
    specified by this decorator become the default guilds that it's added to rather
    than being a global command.

    .. note::

        Due to an implementation quirk and Python limitation, if this is used in conjunction
        with the :meth:`CommandTree.command` or :meth:`CommandTree.context_menu` decorator
        then this must go below that decorator.

    Example:

    .. code-block:: python3

            MY_GUILD_ID = discord.Object(...)  # Guild ID here

            @app_commands.command()
            @app_commands.guilds(MY_GUILD_ID)
            async def bonk(interaction: discord.Interaction):
                await interaction.response.send_message('Bonk', ephemeral=True)

    Parameters
    -----------
    \*guild_ids: Union[:class:`int`, :class:`~discord.abc.Snowflake`]
        The guilds to associate this command with. The command tree will
        use this as the default when added rather than adding it as a global
        command.
    """
    ...

def check(predicate: Check) -> Callable[[T], T]:
    r"""A decorator that adds a check to an application command.

    These checks should be predicates that take in a single parameter taking
    a :class:`~discord.Interaction`. If the check returns a ``False``\-like value then
    during invocation a :exc:`CheckFailure` exception is raised and sent to
    the appropriate error handlers.

    These checks can be either a coroutine or not.

    Examples
    ---------

    Creating a basic check to see if the command invoker is you.

    .. code-block:: python3

        def check_if_it_is_me(interaction: discord.Interaction) -> bool:
            return interaction.user.id == 85309593344815104

        @tree.command()
        @app_commands.check(check_if_it_is_me)
        async def only_for_me(interaction: discord.Interaction):
            await interaction.response.send_message('I know you!', ephemeral=True)

    Transforming common checks into its own decorator:

    .. code-block:: python3

        def is_me():
            def predicate(interaction: discord.Interaction) -> bool:
                return interaction.user.id == 85309593344815104
            return app_commands.check(predicate)

        @tree.command()
        @is_me()
        async def only_me(interaction: discord.Interaction):
            await interaction.response.send_message('Only you!')

    Parameters
    -----------
    predicate: Callable[[:class:`~discord.Interaction`], :class:`bool`]
        The predicate to check if the command should be invoked.
    """
    ...

@overload
def guild_only(func: None = ...) -> Callable[[T], T]:
    ...

@overload
def guild_only(func: T) -> T:
    ...

def guild_only(func: Optional[T] = ...) -> Union[T, Callable[[T], T]]:
    """A decorator that indicates this command can only be used in a guild context.

    This is **not** implemented as a :func:`check`, and is instead verified by Discord server side.
    Therefore, there is no error handler called when a command is used within a private message.

    This decorator can be called with or without parentheses.

    Due to a Discord limitation, this decorator does nothing in subcommands and is ignored.

    Examples
    ---------

    .. code-block:: python3

        @app_commands.command()
        @app_commands.guild_only()
        async def my_guild_only_command(interaction: discord.Interaction) -> None:
            await interaction.response.send_message('I am only available in guilds!')
    """
    ...

def default_permissions(**perms: bool) -> Callable[[T], T]:
    r"""A decorator that sets the default permissions needed to execute this command.

    When this decorator is used, by default users must have these permissions to execute the command.
    However, an administrator can change the permissions needed to execute this command using the official
    client. Therefore, this only serves as a hint.

    Setting an empty permissions field, including via calling this with no arguments, will disallow anyone
    except server administrators from using the command in a guild.

    This is sent to Discord server side, and is not a :func:`check`. Therefore, error handlers are not called.

    Due to a Discord limitation, this decorator does nothing in subcommands and is ignored.

    .. warning::

        This serves as a *hint* and members are *not* required to have the permissions given to actually
        execute this command. If you want to ensure that members have the permissions needed, consider using
        :func:`~discord.app_commands.checks.has_permissions` instead.

    Parameters
    -----------
    \*\*perms: :class:`bool`
        Keyword arguments denoting the permissions to set as the default.

    Example
    ---------

    .. code-block:: python3

        @app_commands.command()
        @app_commands.default_permissions(manage_messages=True)
        async def test(interaction: discord.Interaction):
            await interaction.response.send_message('You may or may not have manage messages.')
    """
    ...

