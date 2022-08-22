
# **Choosing a Statistical Method**
## **Tests & Types**
***
- **Parametric Test**
  - More realistic results
  - first we meet the assumptions
  - we have non ordered values 

|  A |B 
---------|----------|
 2 | 25 | 
 5| 38 | 
 16 | 52 | 

- **Non-parametric Test**
  - Less realistic results
  - calculate the rank of data
  - no need to meet assumptions
  
|  A |B 
---------|----------|
 1 | 1 | 
 2 | 2 | 
 3 | 3 | 

##**Parametric Tests**
***

### **Step-1: Normality Check**
***
- Shapiro Wilk Test
  - Specific & Relieable
- Kolmogorov-Smirnov Test 
  - General

### **Step-2: Homogeneity test**
***
The Varience of the variable in data are equale.
Test to be used:
#### Levene's Test
***
### **Step-3: Purpose**
Know the purpose of your research question.

### **Two types of purposes**
***
- Comparison
  - Difference
  - At least two groups
- Relationship
  - connection
  - find a connection
    - Connection
    - corelation
    - prediction
  
### **Step-4: Data type**
***
Know the type of data you are working with. 

#### **Types**
***
- Catagorical.
  - Qualitative
- Continuous
  - Quantitative

### **Step-5:Statistical Tests**
***
Choose a statistical test from three main families.

### **1- Chi-Squared**

 - comparison
        - only catagorical data
 - Test of Homogeneity 
 - Test of Independence
  - What to use?
  - Nothing effects this,
  - can be used with any number of levels of groups.\
  You must remember the purpose and data type.

### **2- T-Test/ANOVA**

        - Comparison
        - Catagorical and continuous data
    1- One sample T-Test
        for one sample group with a known mean.
    2- Two-Sample T-Test.
        - Un-paired T-Test(Two Different groups)
        - Paired T-Test( Same groups twice)
    3- ANOVA( Analysis of Variance)
        [3+ levels or groups are involved]
        - One-Way ANOVA
            Even one of groups is significant, you'll get significant results, but doesn't tell you which one.
        - Two-Way ANOVA
            Repeated measures of ANOVA(3+ paired groups, scale up paired t-test).

### **3- Correlation**  

- Relationship
- Continuous only(correlation)

 ### **Types**

 ***
- Pearson's Correlation( One independent & one dependent variable).
- Regression( One independent & one dependent variable) but we see equation.
  
> Correlation: Tells us how closely connected two variables are?
> Regression: Tells us a specific mathematical equation that describes the relationship.
***
### **Assumptions about your data**
  - These test trusts you that
    - Your data is normally distributed.
    - or follow a Gaussian distribution.

If you do not follow tha assummtions and break the trusts of 3-tests families, they'll not happy with you.

If assumptions are not met we have to do Check **Normality, homogeniety**.

### 1- Normalize your data 
  - a Standardization
  - Min-Max scaling
  - Log-Transformation

### 2- Use alternative Non-Parametric Tests.

## Non-Parametric Alternatives:
***
1- Chi-Squared Test
   - Chi-Squared

2- T-Test/ANOVA

  -   One Sample ( One Sample ) 
      - Wilcoxon Signed rank test
  -   Two Sample 
      -   Paired Wilcoxon
      -   Un-Parired (Mann Whitney U-test )
  -   ANOVA
      -   kruskal wallis test

3- Correlation
- Pearson's correlation regression
- Spearman's Correlation &
- kendall's tau

### Types of ANOVA
***
- One Way ANOVA ( Even one group is significant, you'll get sugnificant results.)
- Two-Way ANOVA (2 Factor involved)
- Repeat measures of ANOVA (3+ paired groups, scale up of paired T-Test).
- ANCOVA (Analysis of Co-variance)
- MANOVA (Multi-Variate analysis of Variance)
- MANCOVA (Multi-Variate analysis of Co-Variance)

### **Graph**
  ***
```
Normality--If not--> Normalized Data---if not---> Non-Parametric Test.
```
#### Non-Paramatric Test:
****
```
Comparison <----[Purpose]---> Correlation
```
***
- Comparison
  - One-Sample Test( One sample Wilcoxon Test)
  - Unpaired T-Test(Mann Whitney's U-Test)
  - Paired T-Test( Wilcoxon)
  - ANOVA ( Kruskal Wallis Test)
- Correlation
  - Pearson;'s Correlation
  - Spearman's correlation
  - Kendall's Tau regression

If,
```
Normality---Not--> Normalize Data ----Yes---> Paramatric Test 
```
or, 
```    
Normality --Yes--> Paramatric Test.
```
### Paramatric Tests:
****
```
Comparison <----[Purpose]---> Correlation
```
***
- Comparison
  - T-Test
    - One-way sample 
    - Two-Way sample
      - Paired 
      - Un-Paired
  - ANOVA
    - One-Way
    - Two-Way
***

## Research Designs
- CBD (Complete Randomized Design)
- RCBD (Randomized Complete Block Design)
- LSD (Latin Square Design)
***

# 1.Shapiro wilk Test
Tests whether a data sample has a Gaussian distribution.
## Assumtions
1. Observations in each sample are independent and indirectlly distributed(iid).
2. Interpretation

- H0: The sample has a Gaussian Normal distribution.
- H1: The sample does not have a Gaussuan Normal distribution.
```python
#Example of the Shapiro Wilk Normality Test.
for scipy.stats import shapiro
data = [0.873,2.817,0.121.-0.945]
stat,p= shapiro(data)
print('stat=%f,p=%f' % (stat,p))
if p> 0.05:
    print('Probably Gaissian')
else:
    Print('Probably not Gaussian')
```
# 2- Correlation Test
### **2.1 Peason's Correlation Coefficient**
Tests whether two samples have a linear relationship.
## **Assumptions**
   
1. Observations in each sample are independent and indirectlly distributed(iid).
2. Interpretation
3. Observation in each sample are nomrally distributed.
4. Observations in each sample have the same variance.

- H0: The two samples are independent.\
- H1: there is a dependency between the samples.
```python
from scipy.stats import pearsonr
data1= [0.873,2.817,0.121,0.945,0.055,1.436,0.360,1.478,1.637,1.896]
data2= [0.353,3.517,0.125,7.545,0.555,1.536,3.360,1.578,1.537,1.586]
stat,p = pearsonr(data1,data2)
print(stat=%.3f,p=%.3f % (stat,p))
if p> 0.05:
    print('Probably independent')
else:
    print('Probably dependent')
```
###  **2.2 Spearman's Rank Correlation**    
Tests whether two samples have a monotonic relationship.
## **Assumptions**
1. Observations in each sample are independent and indirectlly distributed(iid).
2. Interpretation
3. Observations in each sample can be ranked.
   
- H0: The two samples are independent.
- H1: there is a dependency between the samples.
```python
from scipy.stats import spearmanr
data1= [0.873,2.817,0.121,0.945,0.055,1.436,0.360,1.478,1.637,1.896]
data2= [0.353,3.517,0.125,7.545,0.555,1.536,3.360,1.578,1.537,1.586]
stat,p = spearmanr(data1,data2)
print(stat=%.3f,p=%.3f % (stat,p))
if p> 0.05:
    print('Probably independent (no Correlation)')
else:
    print('Probably dependent(COrrelation exists)')
```
# **2.3 Chi-Squared Test**
Test whether two categorical variables are related or independent.
## **Assumptions**

Observations used in the calculation of the contingency table are independent.25 or more examples in each cell of the contingency table. Interpretation.
    
- H0: the two samples are independent.
- H1: There is a dependency between the samples.
```python
from scipy.stats import chi2_contingency
table= [[10,20,30],[6,9,17]]
stat,p,dof,expected = chi2_contingency(table)
print('stat=%3f,p=%3f' % (stat,p))
if p> 0.05:
    print('Probably independent')
else:
    print('Probably dependent')
```
# **3- Parametric Statistical hypothesis Tests**
## **3.1- Student's T-Test**
Test whether the means of two independent samples are significantly different.
## **Assumtions**
1. Obervations in each sample are independent and identically distributed(iid).
2. Obervations in each sample are normally distributed.
3. Obervations in each sample have the same variance.
4. Interpretation

- H0: the mean of the samples are Equal. 
- H1: the mean of the samples are un-Equal.
```python
from scipy.stat import ttest_ind
# both contain same no of elements.
data1= [same element no.]
data2=[same element no.]
stat,p= ttest_ind(data1,data2)
print('stat=%.3,p=%.3' % (stat,p))
if p>0.5:
    print('Probably same distribution.')
else:
    print('Probably different distribution')
```
## **3.2-Paired Student's T-test**
Test whether the means of two paired samples are significantly different.
## **Assumtions**
1. Obervations in each sample are independent and identically distributed(iid).
2. Obervations in each sample are normally distributed.
3. Obervations in each sample have the same variance.
4. Observations across each sample are paired.
5. Interpretation

- H0: the mean of the samples are equal. 
- H1: the mean of the samples are un-Equal.
```python
from scipy.stat import ttest_rel
# both contain same no of elements.
data1= [same element no.]
data2=[same element no.]
stat,p= ttest_rel(data1,data2)
print('stat=%.3,p=%.3' % (stat,p))
if p>0.5:
    print('Probably same distribution.')
else:
    print('Probably different distribution') 
```
# **4- Analysis of variance Test (ANOVA)**
Test whether the means of two or more independent samples are signoficantly different.
## **Assumtions**
1. Observations in each sample are independent and identically distributed(iid).
2. Observations in each sample are normally distributed.
3. Observations in each sample have the same variance.
4. Interpretation.
    - H0: The means of the samples are equal.
    - H1: one or more of the means of the sample are unequal.

```python
from scipy.stat import f_oneway
> dataset's contain same no of elements.
data1= [same element no.]
data2=[same element no.]
data3=[same element no.]
stat,p= f_oneway(data1,data2,data3)
print('stat=%.3,p=%.3' % (stat,p))
if p>0.5:
    print('Probably same distribution.')
else:
    print('Probably different distribution')
```
> there are more test in ANOVA just need to change there name from f_oneway to two way.

> When we get **H1** or ANOVA fails then we use **post hoc test's**.