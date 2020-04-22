import pandas as pd


def airbase(df_loc, html_name):
    air_df = pd.read_csv(df_loc)
    head_df = air_df.head(n=10)
    html = head_df.to_html()
    with open('./templates/' + str(html_name), 'w+') as ht_wr:
        ht_wr.write(html)



def flow(df_loc, html_name):
    flow_df = pd.read_csv(df_loc)
    head_df = flow_df.head(n=10)
    html = head_df.to_html()
    with open('./templates/' + str(html_name), 'w+') as ht_wr:
        ht_wr.write(html)


def melb(df_loc, html_name):
    melb_df = pd.read_csv(df_loc)
    head_df = melb_df.head(n=10)
    html = head_df.to_html()
    with open('./templates/' + str(html_name), 'w+') as ht_wr:
        ht_wr.write(html)


def titanic(df_loc, html_name):
    titanic_df = pd.read_csv(df_loc)
    head_df = titanic_df.head(n=10)
    html = head_df.to_html()
    with open('./templates/' + str(html_name), 'w+') as ht_wr:
        ht_wr.write(html)


airbase(df_loc='~/Documents/Data-Science/Tamrin & files/session 3/FlaskDockerExample/app/Data/airbase_data.csv',
        html_name='airbase.html')

flow(df_loc='~/Documents/Data-Science/Tamrin & files/session 3/FlaskDockerExample/app/Data/flowdata.csv',
     html_name='flow.html')

melb(df_loc='~/Documents/Data-Science/Tamrin & files/session 3/FlaskDockerExample/app/Data/melb_data.csv',
     html_name='melb.html')

titanic(df_loc='~/Documents/Data-Science/Tamrin & files/session 3/FlaskDockerExample/app/Data/titanic.csv',
        html_name='titanic.html')
