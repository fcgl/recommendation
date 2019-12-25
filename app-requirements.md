- The /toggle endpoint updates the users recommendation based on the most popular items in the city.
If you look at the /toggle endpoint. That's what runs the process that generates the user recommendations.

- There is a boolean switch that changes the process that is ran (popular/machine learning).
We need to have your recommendation algorithm implementation ran everytime that endpoint is called.


### So we need the following:

1. Functions to query all the data you need for your algorithm (in order for this to work in production we need to be careful with memory. Does your algorithm algorithm work in chunks? Can it work by processing 10,000 rows of data at a time. Or does it need all the data at once?  Another solution would be to use a cluster computing framework, which might be the better way to go about it)

2. Function that takes in the queried data and begins the recommendation algorithm you've made

3. Function that populates the UserRecommendation table and associates the UserRecommendation ID with it's corresponding Users. (when I was doing research it mentioned that some users are likely to get very similar recommendations. So in order to save data for production they would give the same recommendations to three users that are very similar. So in the implementation the UserRecommendation ID can be associated with more than 1 user. This doesn't have to be the case if you don't want, we can have a OnetoOne relationship with UserRecommendation and the User). How the popular recommendation currently works is: it creates one UserRecommendation object, and it gives that ID to every User in our database.