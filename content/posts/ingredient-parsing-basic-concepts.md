---
title: "Ingredient Parsing: Introduction and Terminology"
---

As a recipe search engine, [RecipeRadar](https://www.reciperadar.com) aims to collect and understand recipe content from around the web.

We're able to crawl recipes from any website supported by the [recipe-scrapers](https://github.com/hhursev/recipe-scrapers) Python library, and the result of each crawl includes -- among other details -- the list of the ingredients and the list of the steps required to prepare that recipe.  Each list item consists of plain text, as written by the original recipe author.

Given these text descriptions, one useful and important set of information we can gather is the _names_ of the ingredients used in each recipe and their associated _quantities_.

For example, one recipe may include a requirement for "2 cups of cold water", while another may similarly list "30ml water".  Using RecipeRadar's engineering terminology, we refer to the contents of an ingredient as the 'product' (`water`, in both of these examples), and the amount required as the 'quantity' (`2 cups` and `30ml`, respectively).

So far, so good.  However, the situation becomes a little more complicated when we realize that recipe authors add all kinds of useful flair and detail to their ingredient descriptions:

* a pinch of freshly ground black pepper
* 2 large apples, cut into chunks
* a bunch of kale, roughly chopped
* one medium apple

Here we can see products (`black pepper`, `apples`, `kale`) and quantities listed, and there's also additional information for the chef (`freshly ground`, ...) which may help selection and preparation of the ingredients.  We'd like to keep that extra information around so that the recipe author's instructions are faithfully maintained.

In our next blog post, we'll share and explain some of the code that identifies and extracts product names and ingredient quantities from plain text, and how we use the resulting information to provide recipe search and meal planning functionality.
