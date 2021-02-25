---
title: "Ingredient parsing: handling plurality"
tags:
- engineering
- ingredients
- parsing
- crawler
---

*This is the second post in a [series](/tags/parsing/) that explores the technology that RecipeRadar uses to process and store recipe ingredients*

In [part one](/posts/introduction-to-ingredient-parsing/), we introduced a simplified version of the data model and XML format that RecipeRadar uses to represent ingredient information.

In this post, we'll explain how we handle singular and plural ingredient names for English-language ingredient text.

Let's begin by presenting two of RecipeRadar's ingredient search use cases.

**Use case 1: Search-by-ingredients**

RecipeRadar should allow users to search based on the ingredients they have available, without having to specify quantities.  A user may have tofu and a red onion available at home, for example, and may want to exclude recipes that contain beef.

In English, the words 'tofu' and 'beef' do not have plural forms, so we will focus on the 'red onion' ingredient.

For this user's query, we'd like our search results to include recipes that contain _either_ `red onion` (singular) _or_ `red onions` (plural) as ingredients.

**Use case 2: Ingredient autocompletion**

RecipeRadar should provide relevant [autocompletion](https://en.wikipedia.org/wiki/Autocomplete) suggestions when the user begins inputting an ingredient name.

For example, if the user has entered the characters `green ol`, then we may want to display either `green olive` or `green olives` as a suggestion, but we do _not_ want to display both -- they are the same ingredient.

**Design Considerations**

As with many system design problems, there is more than one possible solution, and [trade-offs](https://en.wikipedia.org/wiki/Trade-off) are involved when choosing an approach.

Some of the questions that we asked ourselves were:

- How can we ensure that a query for an ingredient will match recipes that contain it in either singular or plural form?

- How can we determine whether to suggest the singular or plural form of an ingredient during autocompletion?

- How can we minimize application complexity?

- How can we ensure that search responses are returned quickly?

**Chosen Approach**

We currently use the following strategy:

- Store the original plurality for each ingredient named in the source recipe

- _Also_ store the singular form of each ingredient name

- Require that searches use the singular form of the ingredient name

- To determine suggestion plurality, count the number of times singular vs plural was used, and display the more 'popular' form

This approach is relatively wasteful in terms of storage, since we store both the original and singular forms of each ingredient.

However, it is also relatively simple to explain and implement, and can be achieved without managing a set of 'preferred pluralities' for each ingredient.

It also has a nice property that it will automatically adjust to reflect content retrieved from the web.  If people begin using plural forms much more often in future, then RecipeRadar's suggestions will adapt to that over time.

**Implementation Reference**

At the time this article was written, most of the relevant code is found in these places:

- Storage: the [product name and related fields](https://github.com/openculinary/backend/blob/5382aea14d256dd471d5529592ac5632e520eb7d/reciperadar/models/recipes/ingredient.py#L54-L59) in the RecipeRadar ingredient model

- Storage: the [ingredient product properties](https://github.com/openculinary/backend/blob/5382aea14d256dd471d5529592ac5632e520eb7d/scripts/update-recipe-index.py#L49-L59) stored in the [Elasticsearch Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/7.11/mapping.html)

- Autosuggest: the [plurality detection code](https://github.com/openculinary/api/blob/ae5c00d5e25ed51f5d832910f38bfd9969934929/reciperadar/search/ingredients.py#L33-L69), which uses [Elasticsearch Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/7.11/search-aggregations.html)

- User interface: the [autosuggest result processing code](https://github.com/openculinary/frontend/blob/fcc8ffb02d50bb6dfb17a5be362356f31ef33e8e/src/app/autosuggest.js#L31-L37), which uses the [select2](https://github.com/select2/select2/) library to place each ingredient's _singular_ name into input fields, where they are later [retrieved when a search is performed](https://github.com/openculinary/frontend/blob/fcc8ffb02d50bb6dfb17a5be362356f31ef33e8e/src/app/views/search.js#L37-L38)
