## Flask App Design for Displaying Recent News Articles

### HTML Files

- **index.html:**
   - The main page of the application.
   - Displays a list of recent news articles with their titles, authors, and publication dates.
   - Includes links to view the full article on the corresponding news website.

### Routes

- **`/` (GET):**
   - Serves the `index.html` page.
   - Queries a news API to fetch recent articles.

- **`/full-article/<article_id>` (GET):**
   - Redirects the user to the full article associated with the provided `article_id`.