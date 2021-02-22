---
title: Fortnightly Update - 2020-08-28
date: 2020-08-28
author: James
tags:
- status-update
---
This fortnight's update is relatively short; the engineering team is getting back up to speed following some holiday/vacation time.

**Nutritional Information**

Development towards including ingredient nutritional metadata is making [good](https://github.com/openculinary/knowledge-graph/pull/48) [progress](https://github.com/openculinary/knowledge-graph/pull/49) - the team's been in contact with the author of the open source [`ingreedy-js`](https://github.com/tomwhite/ingreedy-js) project that has already constructed an excellent dataset of nutritional metadata. That dataset has now been fuzzy-matched and included into the RecipeRadar ingredients knowledge base.

The next step will be to index that metadata into our search engine so that approximate aggregate nutritional data is available to surface in future application features.

**Direction Metadata**

It looks like Facebook's [`duckling`](https://github.com/facebook/duckling) natural

language parsing project could be very helpful to extract additional information -- temperatures, for example -- from recipe directions. We would prefer to run this tool as a service within our Kubernetes container environment, and in order to do so we've proposed a small fix/change upstream to them and are awaiting feedback.

**Coming up next**

These tasks are likely to continue within the next two weeks, and after that we'll be working on one of our most important long-term pieces of functionality: collaborative (aka 'multiplayer') RecipeRadar sessions.
