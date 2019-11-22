# RecipeRadar Engineering Blog

The RecipeRadar engineering blog is used to share updates and background about the technology and functionality behind the application.

It's a [Hugo](https://gohugo.io) static site and posts are configured to read their timestamps from this `git` repository.

## Install dependencies

Make sure to follow the RecipeRadar [infrastructure](https://www.github.com/openculinary/infrastructure) setup to ensure all cluster dependencies are available in your environment.

## Local Deployment

To deploy the service to the local infrastructure environment, execute the following commands:

```
sudo sh -x ./build.sh
sh -x ./deploy.sh
```

## Operations

### Creating a new blog post

To create a new blog post, run the following command:

```
hugo new posts/your-article-title.md
```

You should now be able to edit the article under `content/posts/your-article-title.md`.  Once you're done writing, remove the `draft` flag from the file, and run `make` to regenerate the blog.  You can view the newly-generated content by opening the `public/index.html` in a web browser.
