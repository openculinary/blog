---
title: "An introduction to ingredient parsing"
tags:
- engineering
- ingredients
- crawler
---

As a recipe search engine, [RecipeRadar](https://www.reciperadar.com) aims to collect and understand recipe content from around the web.

We're able to crawl recipes from any website supported by the [recipe-scrapers](https://github.com/hhursev/recipe-scrapers) Python library, and the result of each crawl includes -- among other details -- a list of the ingredients required and a list of the preparation directions.  Both of these lists are composed of text strings as written by the original recipe author.

For each ingredient there are two key pieces of information we'd like to gather: the _name_ of each ingredient and the associated _quantity_ of it that is required.

Let's take two examples.  One recipe could include an ingredient with the description "2 cups of cold water", while a second recipe may list "30ml water".

Within RecipeRadar's [data model](https://en.wikipedia.org/wiki/Data_model), we refer to the contents of an ingredient as the 'product' (`water` in both of these examples), and the amount required as the 'quantity' (`2 cups` and `30ml` respectively).

So far, so good.  However, the situation becomes a little more complicated when we realize that recipe authors add all kinds of useful flair and detail to their ingredient descriptions:

* a pinch of freshly ground black pepper
* 2 large apples, cut into chunks
* a bunch of kale, roughly chopped
* one medium apple

Here we find products (`black pepper`, `apples`, `kale`) and quantities interleaved with additional information (`freshly ground`, ...) intended to help selection and preparation of ingredients.  We'd like to keep that extra information around so that the recipe author's instructions are faithfully maintained.

In our next blog post, we'll share and explain some of the code that identifies and extracts product names and ingredient quantities from plain text, and how we use the resulting information to provide recipe search and meal planning functionality.
