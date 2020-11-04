---
title: "An introduction to ingredient parsing"
tags:
- engineering
- ingredients
- crawler
---

*This is the first post in a series that explores the technology that RecipeRadar uses to process and store recipe ingredients*

As a recipe search engine, [RecipeRadar](https://www.reciperadar.com) aims to collect and understand recipe content from around the web.

We're able to crawl recipes from any website supported by the [recipe-scrapers](https://github.com/hhursev/recipe-scrapers) Python library, and the results of each crawl include -- among other details -- a list of the recipe's ingredients and a list of the preparation steps.  Both of these lists are represented as lines of text, as written by the original recipe author.

For each ingredient there are two key pieces of information we'd like to gather: the _name_ of each ingredient and the associated _quantity_ of it that is required.  Given these, we can offer search-by-ingredient functionality -- "show me recipes containing tomatoes" -- and also build shopping lists that indicate what quantity of ingredients are required for a set of planned meals.

Let's use some real-world ingredient descriptions as examples.  One recipe could include an ingredient with the description "2 cups of vegetable stock", while a second recipe may list "30ml vegetable stock".

Within RecipeRadar's [data model](https://en.wikipedia.org/wiki/Data_model), we refer to the contents of an ingredient as the 'product' (`vegetable stock` in both of these examples), and the amount required as the 'quantity' (`2 cups` and `30ml` respectively).

So far, so good.  However, the situation becomes a little more complicated when we realize that recipe authors add all kinds of useful flair and detail to their ingredient descriptions:

* a pinch of freshly ground black pepper
* 2 large apples, cut into chunks
* a bunch of kale, roughly chopped
* one medium apple

Here we find products (`black pepper`, `apples`, `kale`) and quantities interleaved with additional information (`freshly ground`, ...).  We'd like to keep that extra information around -- it can help with preparation and selection of ingredients, and it helps to ensure that the recipe author's instructions are faithfully maintained.

In our next blog post, we'll share and explain some of the code that identifies and extracts product names and ingredient quantities from plain text, and how we use the resulting information to provide recipe search and meal planning functionality.
