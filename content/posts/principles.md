---
title: RecipeRadar
author: James
tags:
- company
- culture
- principles
---
RecipeRadar aims to provide recipe search, meal planning, and cooking guidance
to a global audience via services which are simple, intuitive, collaborative
and effective, and always designed with users as our first priority.

We believe that eating well and making informed consumption decisions are a
benefit to everyone, both individually and collectively.

We believe that the best technology is designed with users as the sole and
primary benefactors, and that they should have the ability to inspect, modify
and adjust that technology.

To meet these principles, we have made a number of intentional decisions about
the structure of the company and our service:

- RecipeRadar is developed by OpenCulinary C.I.C., a UK Community Interest
  Company.  The use of this company structure locks in social goals and reduces
  the potential for growth or revenue pressures to lead the service in
  directions which negatively affect users.  If you're curious to learn more,
  please read our [company
  documentation](https://github.com/openculinary/company).

- All of the code for our application and service is publicly available under
  the AGPLv3 license, and we gladly accept changes and contributions
  from our user community.

- We do not use any proprietary software anywhere in the delivery of our
  service, which means that you can inspect and reproduce any part of our
  [technology stack](https://github.com/openculinary/).

- No personal data about you is stored on our servers; the only data
  transmitted from the application to the server is the data required to
  fulfill service requests.  For example, when searching for recipes, the
  application sends the list of ingredients you specify so that the server
  can respond with suitable results.

- Further to this, no cookies are stored in your browser, and no cookie data
  is sent to our servers.

- When *any* data is transferred between the application and our servers, it
  is always encrypted with TLS.  We use a strong cipher suite, and we test our
  configuration using SSL Labs' 'SSL Server Test' tool to discover areas for
  improvement.  If you discover or suspect any issue with our application or
  server security, please [let us know](mailto:security@reciperadar.com) and
  we'll investigate.
