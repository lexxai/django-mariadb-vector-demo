# Django MariaDB Vector Demo

## How Recommendations Work (High Level)

1. Articles are stored in the database with text content.
2. The content is embedded into a vector representation (e.g., via an embedding model).
3. To find similar articles, the app computes a distance (or similarity score) between vectors.
4. The closest vectors are returned as "similar articles."

The result is a simple recommendation system suitable for blogs, documentation, or news-style content.

---

## Examples

## Recommendations of Articles

![arts.png](../assets/images/arts.png)
_List of all articles_

![art1.png](../assets/images/art1.png)
_List of articles similar to Article with pk=1_

![art2.png](../assets/images/art2.png)
_List of articles similar to Article with pk=2_

![art3.png](../assets/images/art3.png)
_List of articles similar to Article with pk=3_

### Admin. Add the article
![admin-art2.png](../assets/images/admin-art2.png)
_Adding new article data through the Django admin_

---

## [Installation and usage](../README.md)