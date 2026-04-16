import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class AutoPushHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        if '.git' in event.src_path:
            return
        print(f"Change detected: {event.src_path}")
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", f"auto: updated {os.path.basename(event.src_path)}"], check=True)
            subprocess.run(["git", "push"], check=True)
            print("✅ Pushed to GitHub!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Git error: {e}")

if __name__ == "__main__":
    path = "."
    event_handler = AutoPushHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("👀 Watching for changes... (Ctrl+C to stop)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()