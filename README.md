# Ansible-Flask Project

This project demonstrates a CI/CD pipeline using **Flask**, **Docker**, **Ansible**, **Jenkins**, **Prometheus**, and **Grafana**.

## Project Structure
- `app.py` → Flask application
- `Dockerfile` → Container setup for Flask
- `deploy_flask.yml` → Ansible playbook for deploying Docker app
- `prometheus.yml` → Prometheus configuration
- `Jenkinsfile` → CI/CD pipeline
- `grafana/` → Grafana dashboards (if any)
- `requirements.txt` → Python dependencies

## How to Run

### 1. Run Flask App
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
Access the app at: http://localhost:50003
-------------------------------------------------------------------------
2. Run Prometheus
docker run -d \
  --name prometheus \
  -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
Access Prometheus at: http://localhost:9090
--------------------------------------------------------------------------
3. Run Grafana
docker run -d \
  --name grafana \
  -p 3000:3000 grafana/grafana
Access Grafana at: http://localhost:3000
---------------------------------------------------------------------------
4. Run Ansible Playbook
ansible-playbook -i hosts.ini deploy_flask.yml
---------------------------------------------------------------------------
5. Metrics
access at http://localhost:50003/metrics















