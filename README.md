# marne_cog

Battlefield 1 marne submodule

## usage

import the cog with

```py
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Marne(bot))
```

or use it inside another cog

```py
class Marne_Private(BattleBit, name="marne"):
```
