🔹 Step 1: Build the Task Environment (Docker Image)

# Navigate to environment directory
cd "D:\Company Asssesments\EOD\harbor_tasks\json-to-csv-filter\environment"

# Build Docker image
docker build -t harbor-task-img .

🔹 Step 2: Run the Oracle (Reference Solution)

# Start container in detached mode
docker run -d --name harbor-test-container harbor-task-img

# Copy solve.sh into the container
docker cp ../solution/solve.sh harbor-test-container:/app/solve.sh

# Execute solve.sh inside the container
docker exec harbor-test-container bash /app/solve.sh

🔹 Step 3: Run Validation Tests

# Copy tests folder into the container
docker cp ../tests harbor-test-container:/app/tests

# Install test dependencies inside the container
docker exec harbor-test-container pip install pandas pytest

# Run pytest to validate output.csv
docker exec harbor-test-container pytest /app/tests/test_outputs.py

📄 Output Handling
🔹 Option 1: View CSV Directly in Terminal (Quick Look)

docker exec harbor-test-container cat /app/output.csv

🔹 Option 2: Copy CSV from Container to Host Machine

docker cp harbor-test-container:/app/output.csv ./output.csv

📌 File will be available at: D:\Company Asssesments\EOD\output.csv

🧹 (Optional) Cleanup Commands

# Stop the container
docker stop harbor-test-container

# Remove the container
docker rm harbor-test-container