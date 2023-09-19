---
title: "Niche Software Libraries"
draft: true
tags:
- engineering
- foss
- open source
---
When it's going well, software development can be as enjoyable and straightforward as building a model from [LEGO bricks](https://www.lego.com): you have an idea or a goal in mind, and you begin to scour through the available components to put together the intended result.  If you're lucky, you find detailed instructions -- requirements and [documentation](https://about.readthedocs.com/) -- to help you along your way.

Meanwhile, one of the reasons that open source software has become so successful over the past few decades is that different software developers are frequently looking for components that match similar requirements when they're building systems.  Regardless of the size of a software project or the industry that it relates to, common challenges appear again and again during development: parsing text, storing structured data, monitoring system uptime.. the list is endless.  And thanks to the Internet, once a previously-unsolved problem has been addressed, it's straightforward to share and distribute the code that filled the gap.

Over time, this creates a form of self-improving software community workshop where developers can demonstrate that their components are the most useful, highest quality, best tested, well maintained and easiest to use -- and then selectively retrofit and improve their own workflows and projects based on each other's contributions.  The rewards for participating are numerous: there's a feelgood factor when authors learn that they've enabled someone else to achieve something, there's a name recognition factor, there's the possibility to discover career opportunities, there's social interaction, and there's the chance to share the development workload.. not to mention the satisfaction gained from using the software as it improves, or the potential to obtain funding to develop it.

![The workshop of a ship's carpenter at the Altonaer Museum in Hamburg, Germany](/images/schiffszimmerers-werkstatt.png)

The resulting software commons - which has no single authority or geography - has produced widely publicised projects such as the [Linux kernel](https://www.kernel.org), [GNU Coreutils](https://www.gnu.org/software/coreutils/coreutils.html), and [PostgreSQL database](https://www.postgresql.org) that have undoubtedly altered the course of computing history - and in doing so, have made software easier, cheaper and less time-consuming to access, deploy, learn, and improve upon.

This post is about some of the smaller, lesser-known libraries that RecipeRadar has investigated and selected for specific functionality so far.  As a reminder: our objective is to provide completely free recipe search and meal planning to the general public, and to build that functionality in the open, using [free and open source software](https://en.wikipedia.org/wiki/Free_and_open-source_software) (FOSS).

**peer-base and yjs**
Today, RecipeRadar exists as a _single-user_ application: you open it on your computer, tablet or smartphone, and although your device communicates with the [RecipeRadar API](https://github.com/openculinary/api/), your copy of the app does not communicate with anyone else's.

In the past we've experimented with introducing [peer-to-peer networking](https://en.wikipedia.org/wiki/Peer-to-peer) to enable scalable and fault-tolerant _multi-user_ interaction: a shared app session could exist across two or more smartphones, perhaps even during outages of the RecipeRadar search service.  The initial [use case](https://www.usability.gov/how-to-and-tools/methods/use-cases.html) for that was to enable multi-person households to co-ordinate food shopping; a companion task to meal planning.

One of the core challenges in a peer-to-peer user application is how to maintain consistent state between each client -- in other words, for each user to have the same model of the world while they use the application.  This is particularly tricky because user devices aren't online continuously.  Your housemate might turn on airplane mode to save battery while doing the weekly shopping, and you might be editing the shopping list from home at the same time.  What happens to the combined edits from both of you when your housemate re-activates their data connection?

The job of a good technology library is to hide (or to ['abstract'](https://en.wikipedia.org/wiki/Abstraction_layer), to use industry terminology) as many of the details of questions like these from developers.  Writing a library that exposes a sensible set of operations that makes it easy and straightforward to achieve objectives while making it difficult or impossible to misuse the system is a large part of [good API design](https://www.redhat.com/en/topics/api/what-is-api-design).

Among libraries that provide support for multi-party data consistency, there are two popular modern schools of design: [Operational Transformations](https://en.wikipedia.org/wiki/Operational_transformation) have proven popular in some cloud-based collaboration suites, and [Conflict-free Replicated DataTypes](https://crdt.tech/) provide an alternative that does not require a central co-ordination authority - arguably a benefit, but also a drawback under some circumstances, because the ability to decide what edits are valid can be difficult in a distributed environment, and especially so in situations where some clients may be untrusted or have software bugs (that is: reality).

We decided to explore the edge of what's technically feasible, and began exploring CRDTs.  Of the available CRDT libraries compatible with the ecosystem of our application (JavaScript within a web browser context), two libraries in particular appeared promising to us:

  - [`peer-base`](https://github.com/peer-base/peer-base/) - a library to assist the construction of distributed peer-to-peer applications; there isn't much evidence of developer activity in the past few years although there is at least one impressive video demonstration of an app that uses the library: [`peer-chess`](https://github.com/jbenet/peer-chess/).
  - [`yjs`](https://github.com/yjs/yjs/) - an actively-maintained and fairly popular CRDT-based library that provides integrations with some existing text editing components, including [ProseMirror](https://prosemirror.net/).

We also learned about [Cattaz](https://github.com/FujitsuLaboratories/cattaz/), a research project by Fujitsu Labs that builds upon YJS to demonstrate rich collaborative editing capabilities as part of a wiki-based document editing tool.

RecipeRadar is registered as a company in the United Kingdom, and although it may be an overly-cautious interpretation of the [draft Online Safety Bill](https://www.gov.uk/government/publications/draft-online-safety-bill) regulations, we determined that allowing our users to communicate with each other, even within a potentially limited scope such as shopping list contents, could open us up to additional technical compliance requirements.  Such functionality may still prove worthwhile in future, but we'd like to wait to see how the regulatory landscape evolves before spending development effort in this area.

**recipe-scrapers**
Retrieving recipes from the world wide web and making them searchable is the core of what RecipeRadar does, and the [`recipe-scrapers`](https://github/com/hhursev/recipe-scrapers/) library is a key component that simplifies that process for us: it is a library that accepts the HTML of a recipe webpage as input, and it provides access to discrete recipe-related fields (the title of the recipe, the author's name, the list of ingredients, and so on) as output.

Where possible, `recipe-scrapers` reads recipe information from a standard [`schema.org` format](https://schema.org/Recipe) that many recipe websites have adopted - and in situations where that isn't possible, it can attempt to find the same data using another library, [`beautifulsoup`](https://beautiful-soup-4.readthedocs.io/en/latest/) that is purpose-designed to query the contents of HTML and XML documents.

We chose to integrate `recipe-scrapers` partly because the programming language that it's written in, [Python](https://www.python.org/), is the one that we're most familiar with and that we use throughout most of the the RecipeRadar [technology stack](https://en.wikipedia.org/wiki/Solution_stack).

`recipe-scrapers` has a friendly, collaborative developer community that we participate in, and we try to walk a careful line of encouraging and improving the functionality that the library provides while not pulling it in a direction that favours RecipeRadar to the detriment of others.  Generally we expect that the use cases we have for the library are similar to those of other people who use it -- that is to say, we think that our incentives are broadly aligned with those of its' community, and we consider it important to maintain that alignment.

It doesn't do _everything_ that we need; `recipe-scrapers` won't extract ingredient names, quantities and units from each line in an ingredient list, for example.  But in software, that can be a good thing: each component should focus on what it does well, and subtasks can be delegated.  Roughly speaking this is referred to as the [principle of separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) in software engineering.

**hashedindex**
Search engine technology is important throughout RecipeRadar - not only to provide the recipe search functionality that we make accessible through our web application, but also during processing of recipe text.

Part of our work involves maintaining a dataset of more than two thousand named products (ingredients).  We use that dataset as a reference when we crawl recipes from the web, and we attempt to annotate each ingredient listing with a relevant product name.

Matching that text is itself a search problem: what is the best product match within a snippet of text such as `block of cheddar, finely grated`?

The answer is that we [build a search index of the product names](https://github.com/openculinary/knowledge-graph/blob/73d44627369728458cff9b6f5278948f5c71ec46/web/models/product_graph.py#L15-L38), and then we use the input text -- the ingredient's description -- as a [query to find and rank the results](https://github.com/openculinary/knowledge-graph/blob/73d44627369728458cff9b6f5278948f5c71ec46/web/ingredients.py#L58-L67).  That might seem slightly counter-intuitive: we're using content from the web as a query, and searching across a set of documents that are typically very short - `cloves` is likely the entire content of the document we're looking for in the given example.  This contrasts to most search engine use cases, where queries are usually shorter than the documents that are retrieved -- but in this case, the situation is reversed.

Why did we use search engine technology to implement this solution?  Well, it's largely because it's an area of technology designed to deal with the kind of linguistic ambiguity that occurs in text that was written by and intended for humans, where spelling mistakes and differing word endings (plurals, for example) can occur, and where ranking of multiple potentially-relevant results can be important.

The [`hashedindex`](https://github.com/MichaelAquilina/hashedindex/) library provides a neat Python-based implementation of text tokenization and search indexing, providing the basis for our in-process Python product search technology.
