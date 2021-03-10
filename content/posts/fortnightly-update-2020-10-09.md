---
title: "Multi-device collaboration, and a discussion on Hacker News"
date: 2020-10-09
author: James
tags:
- status-update
---
Well, it's been a _little_ over a fortnight since the last update; despite that, progress continues on RecipeRadar.

**Multi-device Collaboration**

After some deep thought regarding a technical design for multi-user collaboration on RecipeRadar, we now have a [specification](https://github.com/openculinary/frontend/issues/169) written up. The engineering team is working towards implementing this.

Most good software includes tests to ensure that the code does what it intends to and that it doesn't break during future changes. Unfortunately we're hit a slight roadblock when attempting to write unit tests that cover the database functionality included in the application. The team has [reported the issue](https://github.com/dfahlander/Dexie.js/issues/1126) upstream and is working on a [possible fix](https://github.com/dfahlander/Dexie.js/pull/1138).

**Hacker News Discussion**

There was a recent discussion thread on the popular '[Hacker News](https://news.ycombinator.com/)' technology forum regarding recipe search websites. You can read the entire thread [here](https://news.ycombinator.com/item?id=24630023); RecipeRadar participated in the conversation, and as a result:

- We fixed some issues related to [missing tuna-and-teriyaki-related recipes](https://github.com/openculinary/backend/issues/24)

- We received some [feedback and ideas](https://github.com/openculinary/frontend/issues/172) regarding 'staple' kitchen ingredients

- Some users contributed suggestions regarding kitchen pantry [inventory management integrations](https://github.com/openculinary/api/issues/81)

**Coming up next**

We're hopeful that work on multi-user collaboration will soon become unblocked.

While we're waiting for that to be the case, there are also a few smaller feature items that may we start work on, including showing some of the ingredient nutritional data (that we recently integrated into the knowledge graph) alongside each recipe.
