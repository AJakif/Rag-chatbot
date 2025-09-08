#!/usr/bin/env python3
import time
import os
from pathlib import Path

def tail_logs():
    log_file = Path("logs/rag_chatbot.log")
    logs_dir = Path("logs")
    
    # Create logs directory if it doesn't exist
    logs_dir.mkdir(exist_ok=True)
    
    if not log_file.exists():
        print("Log file doesn't exist yet. Start the application first with 'make run'")
        return
    
    print(f"Tailing log file: {log_file}")
    print("Press Ctrl+C to stop")
    
    try:
        # Continuously read and display new log entries
        with open(log_file, 'r') as f:
            # Move to the end of the file
            f.seek(0, os.SEEK_END)
            
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)  # Wait briefly for new content
                    continue
                print(line, end='')
    except KeyboardInterrupt:
        print("\nStopped tailing logs")

if __name__ == "__main__":
    tail_logs()