# Clank! Archipelago

Clank! A Deck-Building Adventure is a tabletop board game in which players descend into a dungeon to loot the treasures within, but beware! Making too much noise may awake the Dragon, causing chaos and attacks as she tries to stop you from getting away. Will you escape the dungeon alive? or lose both your loot and life in the depths below..

**This Implementation Requires you to own the physical board game of Clank!**

Apologies for any inconveniece this may cause.


## What do locations look like in Clank!

Locations in Clank! are pretty much anything that is brought or collected, such as:
- Artifacts
- Monkey Idols
- Buying Cards
- Beating Boards
- Getting certain Scores
- Buying Market items
- Major/Minor Secrets
- The "Bonus Row" and "Bonus Market"
- Any other things added in Expansions


## What Items can be randomized in Clank!

Items in Clank! are highly customizable:
- Unlock Cards for the Dungeon Row
- Unlock Boards
- Unlock Artifacts
- Unlock Market Items
- Unlock Monkey Idols
- Unlock any Expansion-specific things
- Fillers such as Extra gold
- Traps like Dragon attacks, Rage meter, and +Clank!


## What are the Victory conditions?

There are many Goal options for Clank!
- Collecting all Artifacts
- Collecting all Monkey Idols
- Beating a certain amount of Boards
- Obtaining a certain Score


## What is different from the normal game?

The game is played Solo! it's you against the dungeon.

A "Bonus Row"  Exists ontop of the regular dungeon row, this lets you use skill to instead buy Location Checks.

Ontop of the Bonus Row, there is a "Bonus Market" where you spend gold for Checks.

Major/Minor Secrets instead have a chance to do 3 different things:
- Give you the normal Item on the Secret
- Send a Check (Can be Disabled)
- Gain a Filler/Trap sent from someone else

Apart from that, it's normal Clank! gameplay.


## When the Player recieves an item, what happens?

Filler/Traps are added to a "Queue" which is then pulled from when the player encounters a major/minor secret.

Everything else waits until the Player starts a new run, then all of the awaiting Items are added to the run.


## What else does Randomization do to Clank!

**Deathlink** is supported in Clank!
> When the player recieves a death, they must end their current run.
>
> When the player loses a run (dies) they send a death to everyone else.


## How the hell does a physical game interact with a digital randomizer???

Clank!'s connection to the Archipelago server is handled through a Flask website, hosted by the player's computer

The website handles the Bonus Row/Market and Major/Minor Secrets.

It also informs the player what Items need to be added when starting a run, and has an interface for sending people's location checks.