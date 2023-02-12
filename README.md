# Amazon Vine Analysis

## Overview

The task was to analize all the reviews written by members of the paid Amazon Vine program, specifically for beauty products, to determine if there is any bias toward positive reviews from Vine participants in the dataset. 

Tools: AWS RDS, PySpark, pgAdmin, Google Colab
Dataset: https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Beauty_v1_00.tsv.gz

## Results

The analysis started by filtering the dataset to pick the reviews that were more likely to be helpful, in other words, those where the total votes count was equal or greater than 20 votes. The new table was filtered further to include the reviews with the most helpful votes (equal or greater than 50% of the total votes.) The new table consisted of 74,760 reviews, from which:

* There was a total of 647 Vine program (paid) reviews.

![vine_reviews.png](https://github.com/fabeza/Amazon_Vine_Analysis/blob/9bd397f98187c67aa69b19f375e19fc7bd6380fe/Images/vine_reviews.png)

* There was a total of 74,113 non-Vine (unpaid) reviews.

![nonvine_reviews.png](https://github.com/fabeza/Amazon_Vine_Analysis/blob/9bd397f98187c67aa69b19f375e19fc7bd6380fe/Images/nonvine_reviews.png)

* From the 647 Vine reviews, 229 were 5-star reviews. This means, 35% of the Vine reviews were 5-star reviews.

![vine_five_stars.png](https://github.com/fabeza/Amazon_Vine_Analysis/blob/9bd397f98187c67aa69b19f375e19fc7bd6380fe/Images/vine_five_stars.png)
![vine_percentage.png](https://github.com/fabeza/Amazon_Vine_Analysis/blob/9bd397f98187c67aa69b19f375e19fc7bd6380fe/Images/vine_percentage.png)

* From the 74,113 non-Vine reviews, 43,217 were 5-star reviews. This means, 58% of non-Vine reviews were 5-star reviews.

![nonvine_five_stars.png](https://github.com/fabeza/Amazon_Vine_Analysis/blob/9bd397f98187c67aa69b19f375e19fc7bd6380fe/Images/nonvine_five_stars.png)
![nonvine_percentage.png](https://github.com/fabeza/Amazon_Vine_Analysis/blob/9bd397f98187c67aa69b19f375e19fc7bd6380fe/Images/nonvine_percentage.png)

## Summary

35% of the Vine program member reviews were 5-star reviews while 58% of non-Vine program member reviews were 5-star reviews. This means there is not a significant bias toward positive reviews from Vine participants in the total review dataset. The majority of 5-star reviews for beauty products is coming from unpaid reviewers. 

It would be worthwhile to further analize the dataset by filtering the verified purchases from the non-Vine reviews. This would improve the count and percentage accuracy of the great majority of non-Vine 5-star reviews. 