# Interactive dashboard

Follow the following steps in order to generate the report.

1- Import the InteractiveDashboard class from **OlliePy**

```
from olliepy import InteractiveDashboard
```

2- Select columns to be used in the dashboard

```
categorical_features = ['year', 'country', 'region','remote_sale', 'salesman_position', 'product_type', 'product_subtype']

numerical_features = ['latitude', 'longitude', 'number_of_sales', 'distance_travelled_in_KM', 'sales_amount_in_dollars',
                     'unit_price']
date_features = ['date']
```

3- Create the dashboard.

```
dashboard = InteractiveDashboard(title='Sales dashboard',
                                output_directory='.',
                                dashboard_folder_name='SALES_DASHBOARD',
                                dataframes=[df],
                                dataframes_names=['Sales'],
                                numerical_columns=numerical_features,
                                categorical_columns=categorical_features,
                                date_columns=date_features,
                                generate_encryption_secret=False)
```

```
dashboard.create_dashboard(auto_generate_distribution_plots=True)
```

9- View the dashboard using one of the following methods

- Using a local server

```
dashboard.serve_dashboard_from_local_server(mode='server', load_existing_dashboard=False)
```
You can also use ```start_dashboard.sh``` or ```start_dashboard.bat``` in the dashboard folder to start the server.
Make sure you have selected the right python environment before running the shell/batch script.

- Save then view the dashboard locally using the index.html file

```
dashboard.save_dashboard(zip_dashboard=True)
```
