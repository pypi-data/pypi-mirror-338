import threading
from queue import Queue, Empty
import time


class BufferedThreadedIterator:
    def __init__(self, iterator, buffer_size=0, wait_on_full=0.01, wait_on_empty=0.01):
        """
        Fill a buffer for a lazy iterator using a separate thread.

        Args:
            iterator: The input iterator
            buffer_size: The size of the buffer, passed on to queue.Queue()
                         Default is 0 (fill the buffer as much as possible)
            wait_on_full: How many seconds to wait during filling if the queue is full
                          If buffer_size is 0, the queue can't be full, so wait_on_full has no effect
            wait_on_empty: How many seconds to wait for the fill thread before trying to get a value again
        """
        self.iterator = iterator
        self.queue = Queue(maxsize=buffer_size)
        self.stop_thread = threading.Event()
        self.wait_on_full = wait_on_full
        self.wait_on_empty = wait_on_empty
        self.sentinel = object()  # Unique sentinel object

        self.thread = threading.Thread(target=self.fill_buffer, daemon=True)
        self.thread.start()

    def fill_buffer(self):
        """ Fill the buffer from the iterator until exhausted. """
        try:
            for item in self.iterator:
                while not self.stop_thread.is_set():
                    try:
                        self.queue.put(item, timeout=self.wait_on_full)
                        break
                    except:
                        continue
            self.queue.put(self.sentinel)  # Signal completion
        except Exception as e:
            self.queue.put(e)  # Store exceptions in the queue

    def __iter__(self):
        return self

    def __next__(self):
        """ Yield the next item from the buffer. """
        while not self.stop_thread.is_set():
            try:
                item = self.queue.get(timeout=self.wait_on_empty)
                if item is self.sentinel:
                    raise StopIteration
                elif isinstance(item, Exception):
                    raise item  # Propagate exceptions
                return item
            except Empty:
                if not self.thread.is_alive():
                    raise StopIteration
        raise StopIteration

    def __enter__(self):
        """ Allow usage in a context manager. """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ Ensure cleanup when exiting context. """
        self.stop_thread.set()
        self.thread.join()

# Example Usage
if __name__ == "__main__":
    def lazy_iterator():
        for i in range(10):
            print(f"Generating {i}")  
            time.sleep(0.5)
            yield i

    with BufferedThreadedIterator(lazy_iterator(), buffer_size=5) as buffered_iterator:
        for item in buffered_iterator:
            time.sleep(2)
            print(item)
