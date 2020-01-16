# Calculate Churn Rates for Codeflix.


 


* Step 1: Get familiar with the data

1.Take a look at the first 100 rows of data in the subscriptions table. How many different segments do you see?

```SQL
SELECT * FROM subscriptions
LIMIT 100;
```
We show only the 2 firsts and 3 lasts of the 100:

|id|subscription_start|subscription_end|segment|
|:-:|:-:|:-:|:-:|
|1|2016-12-01|2017-02-01|87|
|2|2016-12-01|2017-01-24|87|
|:|:|:|:|
|98|2016-12-06|2017-03-05|87|
|99|2016-12-06|`Null`|30|
|100|2016-12-06|2017-03-11|30|

We can check channels this way :
```sql
SELECT DISTINCT segment FROM subscriptions;
```
This will return :

|segment|
|:-:|
|87|
|30|

2.Determine the range of months of data provided. Which months will you be able to calculate churn for?

```sql
SELECT MIN(subscription_start) AS 'First Subscription',
       MAX(subscription_start) AS 'Last Subscription'
FROM subscriptions;
```
This will return :

|First Subscription|Last Subscription|
|:-:|:-:|
|2016-12-01|2017-03-30|

* Step 2: Calculate churn rate for each segment

3.You’ll be calculating the churn rate for both segments (87 and 30) over the first 3 months of 2017 (you can’t calculate it for December, since there are no subscription_end values yet).

To get started, create a temporary table of months.

```sql
WITH months AS(
  SELECT 
    '2017-01-01' AS first_day, 
    '2017-01-31' AS last_day 
  UNION 
  SELECT 
    '2017-02-01' AS first_day, 
    '2017-02-28' AS last_day 
  UNION 
  SELECT 
    '2017-03-01' AS first_day, 
    '2017-03-31' AS last_day)
```

4.Create a temporary table, cross_join, from subscriptions and your months. Be sure to SELECT every column.

```sql
WITH months AS(
  SELECT 
    '2017-01-01' AS first_day, 
    '2017-01-31' AS last_day 
  UNION 
  SELECT 
    '2017-02-01' AS first_day, 
    '2017-02-28' AS last_day 
  UNION 
  SELECT 
    '2017-03-01' AS first_day, 
    '2017-03-31' AS last_day),
      cross_join AS (
  SELECT * FROM subscriptions
  CROSS JOIN months)
```

5.Create a temporary table, status, from the cross_join table you created. This table should contain:

    id selected from cross_join
    month as an alias of first_day
    is_active_87 created using a CASE WHEN to find any users from segment 87 who existed prior to the beginning of the month. This is 1 if true and 0 otherwise.
    is_active_30 created using a CASE WHEN to find any users from segment 30 who existed prior to the beginning of the month. This is 1 if true and 0 otherwise.

To do this we add the following code to our With statement:
```sql
        , status AS (
    SELECT id , first_day AS month, 
        CASE
         WHEN (segment=87) AND (subscription_start < first_day) AND ((subscription_end >= first_day) OR (subscription_end IS NULL))
         THEN 1
         ELSE 0 
        END AS is_active_87,
        CASE
         WHEN (segment=30) AND (subscription_start < first_day) AND ((subscription_end >= first_day) OR (subscription_end IS NULL))
         THEN 1
         ELSE 0 
        END AS is_active_30
    FROM cross_j)
```

6.Add an `is_canceled_87` and an `is_canceled_30` column to the status temporary table. This should be `1` if the subscription is canceled during the month and `0` otherwise.

Our complete status table is now :
```sql
        , status AS (
SELECT id , first_day AS month, 
    CASE
     WHEN (segment=87) AND (subscription_start < first_day) AND ((subscription_end >= first_day) OR (subscription_end IS NULL))
     THEN 1
     ELSE 0 
     END AS is_active_87,
    CASE
     WHEN (segment=30) AND (subscription_start < first_day) AND ((subscription_end >= first_day) OR (subscription_end IS NULL))
     THEN 1
     ELSE 0 
     END AS is_active_30,
    CASE
     WHEN (segment=87) AND (subscription_end BETWEEN first_day AND last_day)
     THEN 1
     ELSE 0 
     END AS is_canceled_87,
    CASE
     WHEN (segment=30) AND (subscription_end BETWEEN first_day AND last_day)
     THEN 1
     ELSE 0 
     END AS is_canceled_30
FROM cross_j)
```

7.Create a status_aggregate temporary table that is a SUM of the active and canceled subscriptions for each segment, for each month.

The resulting columns should be:

    sum_active_87
    sum_active_30
    sum_canceled_87
    sum_canceled_30

```sql
        ,status_aggregate AS (
    SELECT status.month AS mon,
           SUM(status.is_active_87) AS sum_active_87,
           SUM(status.is_active_30) AS sum_active_30,
           SUM(status.is_canceled_87) AS sum_canceled_87,
           SUM(status.is_canceled_30) AS sum_canceled_30
    FROM status
    GROUP BY month)
```

8.Calculate the churn rates for the two segments over the three month period. Which segment has a lower churn rate?

The final request is now :
```sql
WITH months AS(
  SELECT 
    '2017-01-01' AS first_day, 
    '2017-01-31' AS last_day 
  UNION 
  SELECT 
    '2017-02-01' AS first_day, 
    '2017-02-28' AS last_day 
  UNION 
  SELECT 
    '2017-03-01' AS first_day, 
    '2017-03-31' AS last_day), cross_j AS (
    SELECT * FROM subscriptions
    CROSS JOIN months), 
  status AS (
   SELECT id , first_day AS month, 
    CASE
     WHEN (segment=87) AND (subscription_start < first_day) AND ((subscription_end >= first_day) OR (subscription_end IS NULL))
     THEN 1
     ELSE 0 
     END AS is_active_87,
    CASE
     WHEN (segment=30) AND (subscription_start < first_day) AND ((subscription_end >= first_day) OR (subscription_end IS NULL))
     THEN 1
     ELSE 0 
     END AS is_active_30,
    CASE
     WHEN (segment=87) AND (subscription_end BETWEEN first_day AND last_day)
     THEN 1
     ELSE 0 
     END AS is_canceled_87,
    CASE
     WHEN (segment=30) AND (subscription_end BETWEEN first_day AND last_day)
     THEN 1
     ELSE 0 
     END AS is_canceled_30
   FROM cross_j),
  status_aggregate AS (
   SELECT status.month AS mon,
          SUM(status.is_active_87) AS sum_active_87,
          SUM(status.is_active_30) AS sum_active_30,
          SUM(status.is_canceled_87) AS sum_canceled_87,
          SUM(status.is_canceled_30) AS sum_canceled_30
   FROM status
   GROUP BY month)
SELECT mon,
       1.0*sum_canceled_87/sum_active_87 AS Churn_87,
       1.0*sum_canceled_30/sum_active_30 AS Churn_30 
FROM status_aggregate;
```
  
  The request returns : 
  
|mon|Churn_87|Churn_30|
|:-:|:-:|:-:|
|2017-01-01|0.251|0.076|
|2017-02-01|0.317|0.073|
|2017-03-01|0.477|0.117|

`Channel 30` has a much lower churn rate. `Channel 87` on the other hand has a very high churn rate. Marketing should take a look.

* Bonus Step : multiple channels

9.How would you modify this code to support a large number of segments?

Each channel has only few lines of code we can easily copy or generate:\
In `status` we have the 2 `CASE` that build `is_active_cn` and `is_canceled_cn`
```sql
,
CASE
     WHEN (segment=cn) AND (subscription_start < first_day) AND ((subscription_end >= first_day) OR (subscription_end IS NULL))
     THEN 1
     ELSE 0 
     END AS is_active_cn,
CASE
     WHEN (segment=cn) AND (subscription_end BETWEEN first_day AND last_day)
     THEN 1
     ELSE 0 
     END AS is_canceled_cn
```
In `status aggregate` the 2 SUM per channel :
```sqlite
,
          SUM(status.is_active_cn) AS sum_active_cn,
          SUM(status.is_canceled_cn) AS sum_canceled_cn
```
In the final call one line of code per channel :
```sqlite
,
       1.0*sum_canceled_cn/sum_active_cn AS Churn_cn 
```
 Replacing `cn` with each channel number and adding the 3 code parts for each new channel would work for a reasonnable number of channels.
 
   But ..
 Is is the right way to do this? We separate each channel by hand, and use GROUP BY for month. We can use GROUP BY for both at the end of status_aggregate.
 
 For this, we need to SELECT the `segment` column in `status` and `status_aggregate`, and rewrite the 2 CASE we keep to check for `is_canceled` and `is_active` (without separating each channel).
 
 
 ```sql
 WITH months AS(
  SELECT 
    '2017-01-01' AS first_day, 
    '2017-01-31' AS last_day 
  UNION 
  SELECT 
    '2017-02-01' AS first_day, 
    '2017-02-28' AS last_day 
  UNION 
  SELECT 
    '2017-03-01' AS first_day, 
    '2017-03-31' AS last_day), cross_j AS (
    SELECT * FROM subscriptions
    CROSS JOIN months), 
  status AS (
   SELECT id , first_day AS month, segment,
    CASE
     WHEN (subscription_start < first_day) AND ((subscription_end >= first_day) OR (subscription_end IS NULL))
     THEN 1
     ELSE 0 
     END AS is_active,
    CASE
     WHEN subscription_end BETWEEN first_day AND last_day
     THEN 1
     ELSE 0 
     END AS is_canceled
   FROM cross_j),
  status_aggregate AS (
   SELECT status.month AS mon,
          segment,
          SUM(status.is_active) AS sum_active,
          SUM(status.is_canceled) AS sum_canceled
   FROM status
   GROUP BY month, segment)
SELECT mon,
       segment,
       ROUND(1.0*sum_canceled/sum_active,3) AS Churn
FROM status_aggregate
ORDER BY 2;
  ```
  This code returns :
 
|mon|segment|Churn|
|:-:|:-:|:-:|
|2017-01-01|30|0.076|
|2017-02-01|30|0.073|
|2017-03-01|30|0.117|
|2017-01-01|87|0.251|
|2017-02-01|87|0.317|
|2017-03-01|87|0.477|
 
This works ! No matter the number of channels.
