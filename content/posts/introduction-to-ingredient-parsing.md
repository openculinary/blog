---
title: "An introduction to ingredient parsing"
tags:
- engineering
- ingredients
- crawler
---

*This is the first post in a series that explores the technology that RecipeRadar uses to process and store recipe ingredients*

As a recipe search engine, [RecipeRadar](https://www.reciperadar.com) aims to collect and understand recipe content from around the web.

We're able to crawl recipes from any website supported by the [recipe-scrapers](https://github.com/hhursev/recipe-scrapers) Python library, and the results of each crawl include -- among other details -- a list of the recipe's ingredients and a list of the preparation step involved.  Both of these lists are represented as lines of text, as written by the original recipe author.

For each ingredient there are two key pieces of information we'd like to identify: the _name_ of the ingredient, and the associated _quantity_ of it that is required.  Using these, we can provide search-by-ingredient functionality -- *"show me recipes containing tomatoes"* -- and also turn a meal plan into a shopping list that includes sum totals of the ingredients required.

Let's use some real-world ingredient descriptions as examples.  One recipe could contain an ingredient with the description "2 cups of vegetable stock", while a second recipe may list "30ml vegetable stock".

Within RecipeRadar's [data model](https://en.wikipedia.org/wiki/Data_model), we refer to the purchasable contents of an ingredient as the 'product' (`vegetable stock` in both of these examples), and the amount required as the 'quantity' (`2 cups` and `30ml` respectively).

So far, so good.  The situation becomes a little more complicated when we realize that recipe authors add all kinds of useful flair and detail to their ingredient descriptions:

* a pinch of freshly ground black pepper
* 2 large apples, cut into chunks
* a bunch of kale, roughly chopped
* one medium apple

Here we find products (`black pepper`, `apples`, `kale`) and quantities interleaved with additional descriptive details (`freshly ground`, ...).  We'd like to keep that extra information around -- it can help with preparation and selection of ingredients, and it helps to ensure that the recipe author's instructions are faithfully maintained.

Although inter-service communication within RecipeRadar typically uses JSON to serialize objects and data, we've found that JSON is not well suited to representing text with inline metadata.  Instead, we use XML which allows us to add markup that is attached to individual phrases.

Taking the first example from the ingredient list above, we could use XML to annotate the product and quantities like so: `a <quantity>pinch</quantity> of freshly ground <product>black pepper</product>`.  In practice, RecipeRadar uses a slightly different XML schema but the principle is the same.

In our next blog post, we'll cover some of the code that extracts product names and ingredient quantities from plain text, and explain how we use the resulting information to provide recipe search and meal planning functionality.
