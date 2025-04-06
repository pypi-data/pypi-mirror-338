# aiomarzban

[![Stars](https://img.shields.io/github/stars/P1nk-L0rD/aiomarzban.svg?style=social)](https://github.com/P1nk-L0rD/aiomarzban/stargazers)
[![Downloads](https://img.shields.io/pypi/dm/aiomarzban.svg)](https://pypi.python.org/pypi/aiomarzban)

Async SDK for the Marzban API based on aiohttp and pydantic.
This library is fully compatible with **[Marzban](https://github.com/Gozargah/Marzban) version 0.8.4** and supports all panel methods.

## Features

- Async library for non-blocking operations
- Automatic under-the-hood access token management
- All functions implemented as native class methods
- Extensive test coverage for most of the code
- Default values can be provided for user creation
- Simplified user creation through method parameters
- Automatic conversion of gigabytes to bytes
- Custom methods for tailored functionality


## Installation

```bash
pip install aiomarzban --upgrade
```

## Examples

```python
from aiomarzban import MarzbanAPI, UserDataLimitResetStrategy, UserStatusModify

marzban = MarzbanAPI(
    address="https://my_domain.com/",
    username="admin",
    password="super_secret_password",
    default_proxies={"vless": {"flow": ""}},
)

async def main():
    # Create admin
    new_admin = await marzban.create_admin(username="new_admin", password="12345678", is_sudo=False)
    print("New admin: ", new_admin)

    # Create user
    new_user = await marzban.add_user(
        username="user1",
        days=90,
        data_limit=100, # In GB
        data_limit_reset_strategy=UserDataLimitResetStrategy.month,
    )
    print("New user: ", new_user)

    # Modify user
    modified_user = await marzban.modify_user(
        username="user1",
        status=UserStatusModify.disabled,
    )
    print("Modified user: ", modified_user)

    # Add days of subscription to user
    modified_user = await marzban.user_add_days("user1", 60)
    print("Modified user: ", modified_user)

    # Get users
    users = await marzban.get_users(offset=0, limit=100)
    print("Users: ", users)
    
    # Create node
    new_node = await marzban.add_node(
        name="New node",
        address="8.8.8.8",
    )
    print("New node: ", new_node)

    # Modify node
    modified_node = await marzban.modify_node(
        node_id=new_node.id,
        usage_coefficient=0.2,
    )
    print("Modified node: ", modified_node)
```

[Examples for all methods](https://github.com/P1nk-L0rD/aiomarzban/blob/main/examples/examples.py)


## Test coverage

**Warning**: It is highly not recommended to run tests on a production server!

- [x] Admin
- [x] Core
- [x] Node
- [ ] Subscription
- [x] System
- [x] User template
- [x] User

To run tests:

Create .env file with panel information

```bash
pytest tests/
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Run tests to ensure everything works (optional).
5. Submit a pull request.

Or [create an issue](https://github.com/P1nk-L0rD/aiomarzban/issues)

## Tasks

1. Fix tests to avoid freezing
2. Tests for subscription
3. ~~Timeout for requests~~
4. ~~Retries for requests~~
5. More custom useful methods
6. ~~Create library in PyPi~~
7. Find and remove bugs :)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, suggestions, or feedback, please reach out to [my telegram](https://t.me/IMC_tech) or mestepanik@gmail.com.
