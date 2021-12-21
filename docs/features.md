## Features
- Once a game has started, cities will show `[IG]` to indicate that the world is "in-game"
- Players can use the `!tagg [number]` or `!uagg [number]` in cities to set the DME TCP(tagg)/UDP(uagg) times manually for the next world they create. If a player sets these, then joins a game, they will be reset. The TCP/UDP agg time is the amount of time the server will aggregate packets before sending the data to the other players. The default in the game is 30 for both. Recommended values range from 0-10. UDP(uagg), is responsible for player movement, and more, while TCP(tagg) is responsible for wrench, and more. 

## API
Current API endpoints:
- `/players`
- `/games`
- `/chat`

## Colored Clan Tags
You are able to customize colors in your clan tags without the need for cheats or hacks. I have built a way to do this only through the custom UI. Listed below are the steps to add colors to your clan tags:

1. Set your clan message to the exact text `Colors 1`
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

### Example
With clan tag set to `Colors 1`:

The clan tag:

```2hey```

will translate to:

![clan_tag_example](https://github.com/jtjanecek/robo/blob/master/docs/assets/example_clan_colors.jpg)
