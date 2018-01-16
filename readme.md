This API was written in Django 1.11.8 based on Python 3.6.4

Each part of the blog API gets its own app as part of the entire django project

Project Structure:
	/DjangoApp
		/api
			/api related code
		/the rest of the code that isn't related to API
		One could possibly add a front-end here


I felt like this structure would work well in case someone wanted to modify the API code and create their own blog with their custom front-end off of it.


Right now, you can make the following API requests


Anyone can make these requests:
1) /api/postings/ HTTP 200 OK
2) /api/postings/id HTTP 200 OK Will return the specific posts

Authenticated users will get some privileges, 1) you get a form field below the normal response when making the same request to add a new blog post or     2)edit an old one when querying a specific blog post.


The rest of the routing issues this API has I am currently working on.
The model and the logic behind the code is all there, I just need to fix
the routing issues that don't allow you to get a response when you get that same API response when you request something like api/person or api/comment.






