import dash
from dash.dependencies import Input,Output
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.express as px
from collections import deque
import pandas as pd
import pyodbc


def connectSQLServer(driver, server, db, username, password):
    connSQLServer = pyodbc.connect(
        r'DRIVER={' + driver + '};'
        r'SERVER=' + server + ';'
        r'DATABASE=' + db + ';'
        r'UID=' + username + ';'
        r'PWD='+ password + ';',
        #r'Trusted_Connection=yes;',
        autocommit=True
    )
    return connSQLServer 


name_title = 'Stats from SQL Server'
app = dash.Dash(__name__)   

app.layout = html.Div(children=[
        
    html.H1(children='Near Real-time Data from SQL Server on Scatterplot '),
     dcc.Graph(
        id='example-graph',animate=True),dcc.Interval(id='interval-component', interval=1*1800000, # in milliseconds every 30 min,
        n_intervals=0),])
    
#Refresh App every 30 Minute
@app.callback(
    Output('example-graph', 'figure'), 
     [Input('interval-component', 'n_intervals')])
             

def update_graph_scatter(connSQLServer):

    dataSQL = [] #set an empty list
    X = deque(maxlen=10)    
    Y = deque(maxlen=10)
                                                                                                               
    sql_conn = connectSQLServer(driver,server,db,username,password) 
    cursor = sql_conn.cursor()
    cursor.execute("""query""")
    rows = cursor.fetchall()
    for row in rows:
        dataSQL.append(list(row))
        labels = ['DF Column Headers']

        df = pd.DataFrame.from_records(dataSQL, columns=labels)
        UserType = df['UserType']
        Percentage = df['% Approval Status']
        Status = df['Status']
        

    fig = px.bar(df, x=UserType, y=Percentage, color=Status, barmode='group',
             height=400)
    fig.update_layout(title_text='Figure Title')
    fig.show()

if __name__ == "__main__":
    app.run_server(debug=True)

