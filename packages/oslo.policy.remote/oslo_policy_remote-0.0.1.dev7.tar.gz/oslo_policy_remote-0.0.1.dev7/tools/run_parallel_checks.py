# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import multiprocessing
import time
import sys
import argparse

def run_checker(worker_id):
    """Run a single instance of the oslopolicy-remote-checker command."""
    cmd = [
        "oslopolicy-remote-checker",
        "--access", "sample_data/auth_v3_token_member.json",
        "--policy", "policy.yaml",
        "--enforcer_namespace", "nova",
        "--enforcer_config", "sample_data/remote_policy.conf"
    ]
    
    print(f"Worker {worker_id} starting...")
    start_time = time.time()
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        end_time = time.time()
        duration = end_time - start_time
        
        if result.returncode == 0:
            print(f"Worker {worker_id} completed successfully in {duration:.2f} seconds")
            return True
        else:
            print(f"Worker {worker_id} failed with return code {result.returncode}")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"Worker {worker_id} encountered an exception: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Run oslopolicy-remote-checker in parallel')
    parser.add_argument('--workers', type=int, default=100, help='Number of parallel workers')
    parser.add_argument('--access', type=str, default='sample_data/auth_v3_token_admin.json', help='Path to access file')
    parser.add_argument('--policy', type=str, default='policy.yaml', help='Path to policy file')
    parser.add_argument('--namespace', type=str, default='nova', help='Enforcer namespace')
    parser.add_argument('--config', type=str, default='sample_data/remote_policy.conf', help='Path to enforcer config')
    
    args = parser.parse_args()
    
    print(f"Starting {args.workers} parallel workers...")
    start_time = time.time()
    
    # Create a pool of workers
    with multiprocessing.Pool(processes=args.workers) as pool:
        # Map the run_checker function to each worker ID
        results = pool.map(run_checker, range(args.workers))
    
    # Count successes and failures
    successes = sum(1 for r in results if r)
    failures = args.workers - successes
    
    end_time = time.time()
    total_duration = end_time - start_time
    
    print(f"\nExecution completed in {total_duration:.2f} seconds")
    print(f"Successful workers: {successes}")
    print(f"Failed workers: {failures}")
    
    return 0 if failures == 0 else 1

if __name__ == "__main__":
    sys.exit(main()) 