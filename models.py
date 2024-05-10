import pickle
import pandas as pd

def load_models():
    global dos_model
    global bf_model
    global bn_model
    global ps_model

    dos_model = pickle.load(open("dos_modelifier.pkl", "rb"))
    bf_model = pickle.load(open("BrootFars_classifier.pkl", "rb"))
    bn_model = pickle.load(open("BatNet_classifier.pkl", "rb"))
    ps_model = pickle.load(open("PortScan_classifier.pkl", "rb"))

def make_pred(file):
    df = pd.read_csv(file,engine="pyarrow")
    
    dos_pred = dos_model.predict(df)
    dos_anomalies = ['DoS Slowloris', 'DoS GoldenEye', 'DoS Hulk', 'DDoS-LOIC-HTTP', 'DDoS-LOIC-UDP', 'DDoS-HOIC']
    anomaly_found = [x in dos_pred for x in dos_anomalies]
    if any(anomaly_found):
        return "DoS"
    
    bf_pred = bf_model.predict(df)
    bf_anomalies = ['SSH-BruteForce', 'Web Attack - SQL', 'Web Attack - XSS', 'Web Attack - Brute Force', 'FTP-BruteForce']
    anomaly_found = [x in bf_pred for x in bf_anomalies]
    if any(anomaly_found):
        return "Brute Force"

    bn_pred = bn_model.predict(df)
    if ('Botnet Ares' in bn_pred):
        return "Botnet"

    ps_pred = ps_model.predict(df)
    if ('Infiltration - NMAP Portscan' in ps_pred):
        return "Port Scan"
    
