## Features
- Once a game has started, cities will show `[IG]` to indicate that the world is "in-game"
- Players can use the `!tagg [number]` or `!uagg [number]` in cities to set the DME TCP(tagg)/UDP(uagg) times manually for the next world they create. If a player sets these, then joins a game, they will be reset. The TCP/UDP agg time is the amount of time the server will aggregate packets before sending the data to the other players. The default in the game is 10 for both. Recommended values range from 0-10. Higher = more lag (generally). UDP(uagg), is responsible for player movement, and more, while TCP(tagg) is responsible for wrench, and more. 

## API
Current API endpoints (port 8281 default):
- `/players`
- `/games`
- `/chat`
- `/alts/[username]`
- `/accounts/id/[account_id]`
- `/accounts/username/[username]`
- `/clans/id/[clan_id]`
- `/clans/name/[clan_name]`

## Colored Clan Tags
You are able to customize colors in your clan tags without the need for cheats or hacks. I have built a way to do this  through the standard menus. Listed below are the steps to add colors to your clan tags:

1. Set your clan message to the exact text `Colors 1` (or `Colors 2` or `Colors 3` depending on what you want your tag to be)
2. Set your clan tag using the mapping below to set your clan tag
3. Exit the clans screen, and go to the clans screen again
4. You should see your custom colored clan tag
5. Set your clan message to whatever else you'd like

### Clan Color Mappings:
Clan message: `Colors 1`:
```
1 -> Default color
2 -> Blue
3 -> Green
4 -> Pink
5 -> White
6 -> Gray
7 -> Black
```

Clan message: `Colors 2`:
```
a -> Default color
b -> Blue
c -> Green
d -> Pink
e -> White
f -> Gray
g -> Black
```

Clan message: `Colors 3`:
```
A -> Default color
B -> Blue
C -> Green
D -> Pink
E -> White
F -> Gray
G -> Black
```

### Example
With clan message set to `Colors 1`:

The clan tag:

```2hey```

will translate to:

![clan_tag_example](https://github.com/jtjanecek/robo/blob/master/docs/assets/example_clan_colors.jpg)
