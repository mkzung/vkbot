# vkbot

Minimal VK longpoll echo bot. Reads new messages from VKontakte's
longpoll API and replies to a couple of hard-coded Russian phrases
(`привет` → `Привет!`, `пока` → `Пока!`).

Kept as a tiny reference for VK longpoll boilerplate.

## Setup

```bash
pip install vk_api
export VK_API_TOKEN=<your-vk-access-token>
python vkbot.py
```

The token must be set via the `VK_API_TOKEN` environment variable.
The earlier version of this file had a hard-coded token in source;
that token has been revoked. **Do not commit access tokens.**

## License

MIT — see [LICENSE](LICENSE).
