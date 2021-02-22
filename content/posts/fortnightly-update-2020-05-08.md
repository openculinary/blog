---
title: Fortnightly Update - 2020-05-08
date: 2020-05-08
author: James
tags:
- status-update
---
Progress on RecipeRadar over the previous fortnight has included improvements to our data processing infrastructure, continued refinement of our screen prototypes, and exploration of collaboration tools and technology selections.

As you may have seen on the discussion list, **Monica** has been iterating on the screen designs for web and mobile, and in particular the prototype meal planner calendar is looking great. I'd like us all to spend a bit more time to make sure these designs are simple and usable. We should initially remove non-essential features, since we continue to have limited software development bandwidth at the moment.

Speaking of which: if you know any developers (senior or junior) who would be interested in learning about the project's code and potentially getting involved further, please send them our way.

Does anyone have experience and/or opinions regarding the [`Flutter`](https://flutter.dev/) application framework? There's a chance RecipeRadar may migrate to use it in future.

**Organizational Goals**

Today I was reading two articles that I'd like to share since it may help explain the direction I'd like to take the organization in, eventually, assuming that the application gains traction.

One article is ['Open Sources: Voices from the Open Source Revolution'](https://www.oreilly.com/openbook/opensources/book/tiemans.html), and it is a record of the challenges and obstacles encountered by Cygnus, an early example of a business founded on open source software. When reading, please bear in mind that software is only one type of digital content -- I believe the principles may apply to other digital creations.

While initially potentially seeming to conflict with the previous article -- but in my opinion, equally based in the same reality -- the second article is '[The Ethics of Unpaid Labor and the OSS Community](https://www.ashedryden.com/blog/the-ethics-of-unpaid-labor-and-the-oss-community)' and it neatly describes an ongoing concern I have about driving the RecipeRadar project and asking for contributions while not necessarily providing much in return, yet.

Open digital environments _should_ lend themselves well to contributions from diverse backgrounds, and should be something that people can contribute to from home and to build up a portfolio of work -- or for pure enjoyment and interest in the field. And eventually the application should also provide value not just to ourselves as users, but also potentially in terms of funds to sustain continued contributions. In practice, opportunity is often equally distributed, and I'd welcome ideas to create a more inclusive and sustainable environment.

**Ingredient and Direction Highlighting**

One major benefit that RecipeRadar will provide compared to many existing recipe software tools is that it will understand information and context about the ingredients and nutrition in recipes, and will eventually -- and always optionally -- offer to help organize kitchen appliances and preparation timing. A simple recurring example I use is that it could identify that a recipe involves pre-heating an oven; and RecipeRadar could offer a reminder to let someone in your home know that it's time to set the oven temperature.

As one of many steps towards this goal of a 'smart and respectful' kitchen assistant, ingredient and equipment metadata is now extracted from recipes, and formatting and punctuation of the original author's intent are retained (thanks again, **Citra**).

To re-state the goal again here: we aim to add valuable additional information to the original recipe, and will always attribute and link back to the original source.

Here are some examples from a search for [slow cooker lentil recipes](https://www.reciperadar.com/#action=search&include=lentil&equipment=slow%20cooker) earlier today - notice that the application has identified the matching ingredient, and highlighted the equipment used in the recipe directions.

![Recipe ingredient list with 'lentils' highlighted](/images/ingredient-highlighting.png)

![Recipe directions with highlighting of the phrase 'slow cooker'](/images/equipment-highlighting.png)

**PWA Store**

Following submission two weeks ago, RecipeRadar has been [accepted into the Progressive Web App Store](https://progressiveapp.store/pwa/RecipeRadar)!

This is great news and some people have already left reviews and our first review, featuring PB&J Sushi.

**Coming up next**

I mentioned in the last update that we'll be looking for translations of messages that appear in the application soon. This is something we didn't quite get around to over the previous two weeks, but it should be progressing within the next fortnight.

Now that the bulk of the backend data pipeline work for ingredient and direction highlighting is completed, focus can return to the frontend user interface and search improvements. Some items we'll look at in the next two weeks include: [partial name search](https://github.com/openculinary/frontend/issues/90), [historic meal planner entries](https://github.com/openculinary/frontend/issues/40), and [messaging improvements](https://github.com/openculinary/frontend/issues/129).
