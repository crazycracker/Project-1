

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
df = pd.read_csv('https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv')
df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Indicator</th>
      <th>PUBLISH STATES</th>
      <th>Year</th>
      <th>WHO region</th>
      <th>World Bank income group</th>
      <th>Country</th>
      <th>Sex</th>
      <th>Display Value</th>
      <th>Numeric</th>
      <th>Low</th>
      <th>High</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>77</td>
      <td>77.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>80</td>
      <td>80.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = pd.read_csv('https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv')
df1.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>STATION</th>
      <th>STATION_NAME</th>
      <th>DATE</th>
      <th>PRCP</th>
      <th>SNWD</th>
      <th>SNOW</th>
      <th>TMAX</th>
      <th>TMIN</th>
      <th>WDFG</th>
      <th>PGTM</th>
      <th>...</th>
      <th>WT09</th>
      <th>WT07</th>
      <th>WT01</th>
      <th>WT06</th>
      <th>WT05</th>
      <th>WT04</th>
      <th>WT16</th>
      <th>WT08</th>
      <th>WT18</th>
      <th>WT03</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GHCND:GME00111445</td>
      <td>BERLIN TEMPELHOF GM</td>
      <td>19310101</td>
      <td>46</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-11</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>...</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
    </tr>
    <tr>
      <th>1</th>
      <td>GHCND:GME00111445</td>
      <td>BERLIN TEMPELHOF GM</td>
      <td>19310102</td>
      <td>107</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>50</td>
      <td>11</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>...</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
      <td>-9999</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 21 columns</p>
</div>



# 1. META DATA FROM THE DATAFRAMES


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4656 entries, 0 to 4655
    Data columns (total 12 columns):
    Indicator                  4656 non-null object
    PUBLISH STATES             4656 non-null object
    Year                       4656 non-null int64
    WHO region                 4656 non-null object
    World Bank income group    4656 non-null object
    Country                    4656 non-null object
    Sex                        4656 non-null object
    Display Value              4656 non-null int64
    Numeric                    4656 non-null float64
    Low                        0 non-null float64
    High                       0 non-null float64
    Comments                   0 non-null float64
    dtypes: float64(4), int64(2), object(6)
    memory usage: 436.6+ KB
    


```python
df1.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 117208 entries, 0 to 117207
    Data columns (total 21 columns):
    STATION         117208 non-null object
    STATION_NAME    117208 non-null object
    DATE            117208 non-null int64
    PRCP            117208 non-null int64
    SNWD            117208 non-null int64
    SNOW            117208 non-null int64
    TMAX            117208 non-null int64
    TMIN            117208 non-null int64
    WDFG            117208 non-null int64
    PGTM            117208 non-null int64
    WSFG            117208 non-null int64
    WT09            117208 non-null int64
    WT07            117208 non-null int64
    WT01            117208 non-null int64
    WT06            117208 non-null int64
    WT05            117208 non-null int64
    WT04            117208 non-null int64
    WT16            117208 non-null int64
    WT08            117208 non-null int64
    WT18            117208 non-null int64
    WT03            117208 non-null int64
    dtypes: int64(19), object(2)
    memory usage: 18.8+ MB
    

# 2. Row names from the dataframes


```python
np.array(list(df.index))
```




    array([   0,    1,    2, ..., 4653, 4654, 4655])




```python
np.array(list(df1.index))
```




    array([     0,      1,      2, ..., 117205, 117206, 117207])



# 3. Change the column name 


```python
# changing the column name of df from indictor to indicator_id
df.rename(columns={'Indicator':'Indicator_Id'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Indicator_Id</th>
      <th>PUBLISH STATES</th>
      <th>Year</th>
      <th>WHO region</th>
      <th>World Bank income group</th>
      <th>Country</th>
      <th>Sex</th>
      <th>Display Value</th>
      <th>Numeric</th>
      <th>Low</th>
      <th>High</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>77</td>
      <td>77.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>80</td>
      <td>80.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Female</td>
      <td>28</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>23</td>
      <td>23.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>High-income</td>
      <td>United Arab Emirates</td>
      <td>Female</td>
      <td>78</td>
      <td>78.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Antigua and Barbuda</td>
      <td>Male</td>
      <td>72</td>
      <td>72.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Antigua and Barbuda</td>
      <td>Male</td>
      <td>17</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Antigua and Barbuda</td>
      <td>Both sexes</td>
      <td>22</td>
      <td>22.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Australia</td>
      <td>Male</td>
      <td>81</td>
      <td>81.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Australia</td>
      <td>Both sexes</td>
      <td>80</td>
      <td>80.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Australia</td>
      <td>Both sexes</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Austria</td>
      <td>Female</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Austria</td>
      <td>Female</td>
      <td>25</td>
      <td>25.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Belgium</td>
      <td>Female</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Eastern Mediterranean</td>
      <td>High-income</td>
      <td>Bahrain</td>
      <td>Male</td>
      <td>73</td>
      <td>73.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Eastern Mediterranean</td>
      <td>High-income</td>
      <td>Bahrain</td>
      <td>Female</td>
      <td>74</td>
      <td>74.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Eastern Mediterranean</td>
      <td>High-income</td>
      <td>Bahrain</td>
      <td>Male</td>
      <td>17</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Bahamas</td>
      <td>Male</td>
      <td>72</td>
      <td>72.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Bahamas</td>
      <td>Both sexes</td>
      <td>21</td>
      <td>21.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Barbados</td>
      <td>Male</td>
      <td>71</td>
      <td>71.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Barbados</td>
      <td>Female</td>
      <td>25</td>
      <td>25.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Barbados</td>
      <td>Both sexes</td>
      <td>23</td>
      <td>23.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Brunei Darussalam</td>
      <td>Female</td>
      <td>20</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Brunei Darussalam</td>
      <td>Female</td>
      <td>22</td>
      <td>22.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Brunei Darussalam</td>
      <td>Female</td>
      <td>21</td>
      <td>21.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Canada</td>
      <td>Female</td>
      <td>82</td>
      <td>82.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Canada</td>
      <td>Male</td>
      <td>21</td>
      <td>21.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Canada</td>
      <td>Female</td>
      <td>24</td>
      <td>24.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Switzerland</td>
      <td>Male</td>
      <td>74</td>
      <td>74.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Switzerland</td>
      <td>Both sexes</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4626</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>Upper-middle-income</td>
      <td>Serbia</td>
      <td>Female</td>
      <td>67</td>
      <td>67.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4627</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Upper-middle-income</td>
      <td>Suriname</td>
      <td>Both sexes</td>
      <td>66</td>
      <td>66.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4628</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Sweden</td>
      <td>Both sexes</td>
      <td>72</td>
      <td>72.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4629</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Africa</td>
      <td>Lower-middle-income</td>
      <td>Swaziland</td>
      <td>Female</td>
      <td>47</td>
      <td>47.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4630</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Africa</td>
      <td>Upper-middle-income</td>
      <td>Seychelles</td>
      <td>Male</td>
      <td>61</td>
      <td>61.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4631</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Eastern Mediterranean</td>
      <td>Lower-middle-income</td>
      <td>Syrian Arab Republic</td>
      <td>Female</td>
      <td>64</td>
      <td>64.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4632</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Chad</td>
      <td>Female</td>
      <td>44</td>
      <td>44.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4633</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>South-East Asia</td>
      <td>Lower-middle-income</td>
      <td>Thailand</td>
      <td>Male</td>
      <td>59</td>
      <td>59.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4634</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>South-East Asia</td>
      <td>Lower-middle-income</td>
      <td>Thailand</td>
      <td>Female</td>
      <td>65</td>
      <td>65.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4635</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>Low-income</td>
      <td>Tajikistan</td>
      <td>Both sexes</td>
      <td>56</td>
      <td>56.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4636</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>Low-income</td>
      <td>Tajikistan</td>
      <td>Female</td>
      <td>60</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4637</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Tonga</td>
      <td>Female</td>
      <td>61</td>
      <td>61.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4638</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Trinidad and Tobago</td>
      <td>Female</td>
      <td>64</td>
      <td>64.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4639</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Trinidad and Tobago</td>
      <td>Both sexes</td>
      <td>61</td>
      <td>61.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4640</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Eastern Mediterranean</td>
      <td>Lower-middle-income</td>
      <td>Tunisia</td>
      <td>Male</td>
      <td>63</td>
      <td>63.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4641</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>Upper-middle-income</td>
      <td>Tuvalu</td>
      <td>Male</td>
      <td>57</td>
      <td>57.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4642</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Uganda</td>
      <td>Female</td>
      <td>40</td>
      <td>40.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4643</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>Lower-middle-income</td>
      <td>Ukraine</td>
      <td>Both sexes</td>
      <td>60</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4644</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Upper-middle-income</td>
      <td>Uruguay</td>
      <td>Male</td>
      <td>65</td>
      <td>65.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4645</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Upper-middle-income</td>
      <td>Uruguay</td>
      <td>Female</td>
      <td>70</td>
      <td>70.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4646</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Upper-middle-income</td>
      <td>Uruguay</td>
      <td>Both sexes</td>
      <td>68</td>
      <td>68.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4647</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Americas</td>
      <td>Upper-middle-income</td>
      <td>Saint Vincent and the Grenadines</td>
      <td>Both sexes</td>
      <td>61</td>
      <td>61.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4648</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Upper-middle-income</td>
      <td>Venezuela (Bolivarian Republic of)</td>
      <td>Both sexes</td>
      <td>66</td>
      <td>66.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4649</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Vanuatu</td>
      <td>Male</td>
      <td>59</td>
      <td>59.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4650</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Samoa</td>
      <td>Male</td>
      <td>62</td>
      <td>62.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4651</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Samoa</td>
      <td>Female</td>
      <td>66</td>
      <td>66.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4652</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>Low-income</td>
      <td>Yemen</td>
      <td>Both sexes</td>
      <td>54</td>
      <td>54.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4653</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Africa</td>
      <td>Upper-middle-income</td>
      <td>South Africa</td>
      <td>Male</td>
      <td>49</td>
      <td>49.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4654</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Zambia</td>
      <td>Both sexes</td>
      <td>36</td>
      <td>36.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4655</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Zimbabwe</td>
      <td>Female</td>
      <td>51</td>
      <td>51.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>4656 rows × 12 columns</p>
</div>




```python
df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Indicator</th>
      <th>PUBLISH STATES</th>
      <th>Year</th>
      <th>WHO region</th>
      <th>World Bank income group</th>
      <th>Country</th>
      <th>Sex</th>
      <th>Display Value</th>
      <th>Numeric</th>
      <th>Low</th>
      <th>High</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>77</td>
      <td>77.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>80</td>
      <td>80.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# 4. Permenantly change the column name


```python
df.rename(columns={'Indicator':'Indicator_Id'},inplace=True)
df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Indicator_Id</th>
      <th>PUBLISH STATES</th>
      <th>Year</th>
      <th>WHO region</th>
      <th>World Bank income group</th>
      <th>Country</th>
      <th>Sex</th>
      <th>Display Value</th>
      <th>Numeric</th>
      <th>Low</th>
      <th>High</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>77</td>
      <td>77.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>80</td>
      <td>80.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Female</td>
      <td>28</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>23</td>
      <td>23.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>High-income</td>
      <td>United Arab Emirates</td>
      <td>Female</td>
      <td>78</td>
      <td>78.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# 5. Change the names of multiple columns


```python
# performing changes in the df
# PUBLISH STATES -> Publish States
# WHO region     -> WHO Region

df.rename(columns={'PUBLISH STATES':'Publish States','WHO region':'WHO Region'},inplace=True)
df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Indicator_Id</th>
      <th>Publish States</th>
      <th>Year</th>
      <th>WHO Region</th>
      <th>World Bank income group</th>
      <th>Country</th>
      <th>Sex</th>
      <th>Display Value</th>
      <th>Numeric</th>
      <th>Low</th>
      <th>High</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>77</td>
      <td>77.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>80</td>
      <td>80.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Female</td>
      <td>28</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>23</td>
      <td>23.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>High-income</td>
      <td>United Arab Emirates</td>
      <td>Female</td>
      <td>78</td>
      <td>78.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# 6. Arrange values of a column in ascending order


```python
# arranging the Year column values in ascending order
df.sort_values('Year',inplace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Indicator_Id</th>
      <th>Publish States</th>
      <th>Year</th>
      <th>WHO Region</th>
      <th>World Bank income group</th>
      <th>Country</th>
      <th>Sex</th>
      <th>Display Value</th>
      <th>Numeric</th>
      <th>Low</th>
      <th>High</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Both sexes</td>
      <td>77</td>
      <td>77.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1270</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Germany</td>
      <td>Male</td>
      <td>72</td>
      <td>72.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3193</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>Lower-middle-income</td>
      <td>Republic of Moldova</td>
      <td>Male</td>
      <td>65</td>
      <td>65.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3194</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>Lower-middle-income</td>
      <td>Republic of Moldova</td>
      <td>Both sexes</td>
      <td>68</td>
      <td>68.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3197</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>Lower-middle-income</td>
      <td>Republic of Moldova</td>
      <td>Male</td>
      <td>15</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1264</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Cyprus</td>
      <td>Both sexes</td>
      <td>76</td>
      <td>76.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3199</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>Lower-middle-income</td>
      <td>Republic of Moldova</td>
      <td>Both sexes</td>
      <td>17</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1262</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Cook Islands</td>
      <td>Male</td>
      <td>17</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1259</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Cook Islands</td>
      <td>Male</td>
      <td>67</td>
      <td>67.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3203</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>South-East Asia</td>
      <td>Lower-middle-income</td>
      <td>Maldives</td>
      <td>Female</td>
      <td>12</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1273</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Denmark</td>
      <td>Both sexes</td>
      <td>20</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3204</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Marshall Islands</td>
      <td>Female</td>
      <td>65</td>
      <td>65.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1253</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Brunei Darussalam</td>
      <td>Both sexes</td>
      <td>73</td>
      <td>73.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1247</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Bahamas</td>
      <td>Male</td>
      <td>17</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3219</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Vanuatu</td>
      <td>Both sexes</td>
      <td>16</td>
      <td>16.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3226</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>Upper-middle-income</td>
      <td>Bulgaria</td>
      <td>Both sexes</td>
      <td>71</td>
      <td>71.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1240</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Belgium</td>
      <td>Female</td>
      <td>23</td>
      <td>23.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1239</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Belgium</td>
      <td>Both sexes</td>
      <td>76</td>
      <td>76.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1238</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Belgium</td>
      <td>Female</td>
      <td>79</td>
      <td>79.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1237</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Austria</td>
      <td>Both sexes</td>
      <td>76</td>
      <td>76.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1236</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Austria</td>
      <td>Male</td>
      <td>72</td>
      <td>72.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3207</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Mongolia</td>
      <td>Female</td>
      <td>64</td>
      <td>64.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3231</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>Upper-middle-income</td>
      <td>Belarus</td>
      <td>Female</td>
      <td>76</td>
      <td>76.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3188</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Lower-middle-income</td>
      <td>Lesotho</td>
      <td>Female</td>
      <td>17</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1277</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Estonia</td>
      <td>Both sexes</td>
      <td>70</td>
      <td>70.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1302</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Hungary</td>
      <td>Male</td>
      <td>65</td>
      <td>65.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3158</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>Lower-middle-income</td>
      <td>Georgia</td>
      <td>Male</td>
      <td>67</td>
      <td>67.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1300</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Croatia</td>
      <td>Male</td>
      <td>69</td>
      <td>69.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3159</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Europe</td>
      <td>Lower-middle-income</td>
      <td>Georgia</td>
      <td>Both sexes</td>
      <td>19</td>
      <td>19.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3160</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Americas</td>
      <td>Lower-middle-income</td>
      <td>Guatemala</td>
      <td>Female</td>
      <td>19</td>
      <td>19.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3175</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>Lower-middle-income</td>
      <td>Iran (Islamic Republic of)</td>
      <td>Male</td>
      <td>19</td>
      <td>19.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3174</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>Lower-middle-income</td>
      <td>Iran (Islamic Republic of)</td>
      <td>Female</td>
      <td>76</td>
      <td>76.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1285</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>France</td>
      <td>Both sexes</td>
      <td>82</td>
      <td>82.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1286</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>France</td>
      <td>Both sexes</td>
      <td>25</td>
      <td>25.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3171</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>Lower-middle-income</td>
      <td>Iran (Islamic Republic of)</td>
      <td>Male</td>
      <td>72</td>
      <td>72.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1288</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>United Kingdom of Great Britain and Northern I...</td>
      <td>Female</td>
      <td>25</td>
      <td>25.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1290</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>United Kingdom of Great Britain and Northern I...</td>
      <td>Both sexes</td>
      <td>24</td>
      <td>24.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1292</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Africa</td>
      <td>High-income</td>
      <td>Equatorial Guinea</td>
      <td>Female</td>
      <td>57</td>
      <td>57.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3166</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Lower-middle-income</td>
      <td>Honduras</td>
      <td>Male</td>
      <td>21</td>
      <td>21.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3165</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Lower-middle-income</td>
      <td>Honduras</td>
      <td>Both sexes</td>
      <td>74</td>
      <td>74.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3163</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Lower-middle-income</td>
      <td>Guyana</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3162</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Lower-middle-income</td>
      <td>Guyana</td>
      <td>Female</td>
      <td>67</td>
      <td>67.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1301</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Croatia</td>
      <td>Both sexes</td>
      <td>21</td>
      <td>21.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3137</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Africa</td>
      <td>Lower-middle-income</td>
      <td>Cameroon</td>
      <td>Male</td>
      <td>55</td>
      <td>55.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1303</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Hungary</td>
      <td>Both sexes</td>
      <td>75</td>
      <td>75.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3155</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Micronesia (Federated States of)</td>
      <td>Male</td>
      <td>68</td>
      <td>68.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3154</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>Lower-middle-income</td>
      <td>Egypt</td>
      <td>Male</td>
      <td>16</td>
      <td>16.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1304</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Hungary</td>
      <td>Both sexes</td>
      <td>20</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1306</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Ireland</td>
      <td>Female</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3150</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Lower-middle-income</td>
      <td>Ecuador</td>
      <td>Male</td>
      <td>21</td>
      <td>21.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3148</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Lower-middle-income</td>
      <td>Ecuador</td>
      <td>Female</td>
      <td>78</td>
      <td>78.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3147</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>Lower-middle-income</td>
      <td>Djibouti</td>
      <td>Female</td>
      <td>17</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3146</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>Lower-middle-income</td>
      <td>Djibouti</td>
      <td>Both sexes</td>
      <td>61</td>
      <td>61.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3145</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Eastern Mediterranean</td>
      <td>Lower-middle-income</td>
      <td>Djibouti</td>
      <td>Female</td>
      <td>63</td>
      <td>63.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1309</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Ireland</td>
      <td>Female</td>
      <td>25</td>
      <td>25.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1316</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Italy</td>
      <td>Both sexes</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3141</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Africa</td>
      <td>Lower-middle-income</td>
      <td>Cabo Verde</td>
      <td>Both sexes</td>
      <td>74</td>
      <td>74.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3139</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Africa</td>
      <td>Lower-middle-income</td>
      <td>Cameroon</td>
      <td>Female</td>
      <td>17</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3156</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Micronesia (Federated States of)</td>
      <td>Male</td>
      <td>16</td>
      <td>16.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4655</th>
      <td>Healthy life expectancy (HALE) at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Zimbabwe</td>
      <td>Female</td>
      <td>51</td>
      <td>51.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>4656 rows × 12 columns</p>
</div>



# 7. Arrange multiple column values in ascending order.


```python
df.sort_values(by=['Display Value','Numeric'],inplace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Indicator_Id</th>
      <th>Publish States</th>
      <th>Year</th>
      <th>WHO Region</th>
      <th>World Bank income group</th>
      <th>Country</th>
      <th>Sex</th>
      <th>Display Value</th>
      <th>Numeric</th>
      <th>Low</th>
      <th>High</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3071</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Sierra Leone</td>
      <td>Both sexes</td>
      <td>11</td>
      <td>11.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1476</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Sierra Leone</td>
      <td>Female</td>
      <td>11</td>
      <td>11.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1474</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Sierra Leone</td>
      <td>Male</td>
      <td>11</td>
      <td>11.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1813</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Eritrea</td>
      <td>Male</td>
      <td>11</td>
      <td>11.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3070</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Sierra Leone</td>
      <td>Female</td>
      <td>11</td>
      <td>11.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3072</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Sierra Leone</td>
      <td>Both sexes</td>
      <td>11</td>
      <td>11.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>265</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Sierra Leone</td>
      <td>Male</td>
      <td>11</td>
      <td>11.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3203</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>South-East Asia</td>
      <td>Lower-middle-income</td>
      <td>Maldives</td>
      <td>Female</td>
      <td>12</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>577</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Eritrea</td>
      <td>Both sexes</td>
      <td>12</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4275</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Papua New Guinea</td>
      <td>Male</td>
      <td>12</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2987</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Eritrea</td>
      <td>Male</td>
      <td>12</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3981</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>Upper-middle-income</td>
      <td>Kazakhstan</td>
      <td>Male</td>
      <td>12</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2032</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Papua New Guinea</td>
      <td>Male</td>
      <td>12</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>256</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>South-East Asia</td>
      <td>Low-income</td>
      <td>Democratic People's Republic of Korea</td>
      <td>Male</td>
      <td>12</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1475</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Sierra Leone</td>
      <td>Male</td>
      <td>12</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1181</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>South-East Asia</td>
      <td>Lower-middle-income</td>
      <td>Maldives</td>
      <td>Both sexes</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3079</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Eastern Mediterranean</td>
      <td>Low-income</td>
      <td>South Sudan</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3675</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Western Pacific</td>
      <td>Upper-middle-income</td>
      <td>Tuvalu</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>991</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Eritrea</td>
      <td>Female</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1899</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Chad</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2033</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Papua New Guinea</td>
      <td>Both sexes</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2959</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Eastern Mediterranean</td>
      <td>Low-income</td>
      <td>Afghanistan</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1631</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>South-East Asia</td>
      <td>Lower-middle-income</td>
      <td>Timor-Leste</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4454</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Upper-middle-income</td>
      <td>South Africa</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>604</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Liberia</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>686</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>1990</td>
      <td>Africa</td>
      <td>Lower-middle-income</td>
      <td>Angola</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2595</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Africa</td>
      <td>Upper-middle-income</td>
      <td>South Africa</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4431</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>Upper-middle-income</td>
      <td>Russian Federation</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1900</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Africa</td>
      <td>Low-income</td>
      <td>Chad</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Life expectancy at age 60 (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Western Pacific</td>
      <td>Lower-middle-income</td>
      <td>Mongolia</td>
      <td>Male</td>
      <td>13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3247</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Upper-middle-income</td>
      <td>Colombia</td>
      <td>Female</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3241</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>Upper-middle-income</td>
      <td>Chile</td>
      <td>Female</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1340</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Netherlands</td>
      <td>Female</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1306</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Ireland</td>
      <td>Female</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1316</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Italy</td>
      <td>Both sexes</td>
      <td>83</td>
      <td>83.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1746</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Monaco</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Iceland</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>446</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Americas</td>
      <td>High-income</td>
      <td>Canada</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>455</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Cyprus</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>523</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>New Zealand</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>499</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Japan</td>
      <td>Both sexes</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>544</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Sweden</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1765</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Portugal</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1742</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Luxembourg</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2852</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Finland</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>946</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>San Marino</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>900</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Israel</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2911</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Norway</td>
      <td>Female</td>
      <td>84</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>904</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Japan</td>
      <td>Female</td>
      <td>85</td>
      <td>85.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2000</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>San Marino</td>
      <td>Female</td>
      <td>85</td>
      <td>85.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>848</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Switzerland</td>
      <td>Female</td>
      <td>85</td>
      <td>85.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2807</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Australia</td>
      <td>Female</td>
      <td>85</td>
      <td>85.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>875</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>France</td>
      <td>Female</td>
      <td>85</td>
      <td>85.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>902</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Italy</td>
      <td>Female</td>
      <td>85</td>
      <td>85.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1369</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Singapore</td>
      <td>Female</td>
      <td>85</td>
      <td>85.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1274</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Spain</td>
      <td>Female</td>
      <td>85</td>
      <td>85.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1323</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Republic of Korea</td>
      <td>Female</td>
      <td>85</td>
      <td>85.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1227</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Andorra</td>
      <td>Female</td>
      <td>86</td>
      <td>86.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1334</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Europe</td>
      <td>High-income</td>
      <td>Monaco</td>
      <td>Female</td>
      <td>86</td>
      <td>86.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1320</th>
      <td>Life expectancy at birth (years)</td>
      <td>Published</td>
      <td>2012</td>
      <td>Western Pacific</td>
      <td>High-income</td>
      <td>Japan</td>
      <td>Female</td>
      <td>87</td>
      <td>87.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>4656 rows × 12 columns</p>
</div>


