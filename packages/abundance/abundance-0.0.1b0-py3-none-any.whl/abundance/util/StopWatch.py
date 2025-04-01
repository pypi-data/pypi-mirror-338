import time


class StopWatch:
    def __init__(self, id=""):
        self.id = id
        self.keep_task_list = True
        self.task_list = []
        self.start_time_nanos = 0
        self.current_task_name = None
        self.last_task_info = None
        self.task_count = 0
        self.total_time_nanos = 0

    def getId(self):
        return self.id

    def setKeepTaskList(self, keep_task_list):
        self.keep_task_list = keep_task_list

    def start(self, task_name=""):
        if self.current_task_name is not None:
            raise ValueError("Can't start StopWatch: it's already running")
        self.current_task_name = task_name
        self.start_time_nanos = time.time_ns()

    def stop(self):
        if self.current_task_name is None:
            raise ValueError("Can't stop StopWatch: it's not running")
        last_time = time.time_ns() - self.start_time_nanos
        self.total_time_nanos += last_time
        self.last_task_info = TaskInfo(self.current_task_name, last_time)
        if self.keep_task_list:
            self.task_list.append(self.last_task_info)
        self.task_count += 1
        self.current_task_name = None

    def isRunning(self):
        return self.current_task_name is not None

    def currentTaskName(self):
        return self.current_task_name

    def getLastTaskTimeNanos(self):
        if self.last_task_info is None:
            raise ValueError("No tasks run: can't get last task interval")
        return self.last_task_info.getTimeNanos()

    def getLastTaskTimeMillis(self):
        if self.last_task_info is None:
            raise ValueError("No tasks run: can't get last task interval")
        return self.last_task_info.getTimeMillis()

    def getLastTaskName(self):
        if self.last_task_info is None:
            raise ValueError("No tasks run: can't get last task name")
        return self.last_task_info.getTaskName()

    def getLastTaskInfo(self):
        if self.last_task_info is None:
            raise ValueError("No tasks run: can't get last task info")
        return self.last_task_info

    def getTotalTimeNanos(self):
        return self.total_time_nanos

    def getTotalTimeMillis(self):
        return self.total_time_nanos // 1_000_000

    def getTotalTimeSeconds(self):
        return self.total_time_nanos / 1_000_000_000

    def getTaskCount(self):
        return self.task_count

    def getTaskInfo(self):
        if not self.keep_task_list:
            raise NotImplementedError("Task info is not being kept!")
        return self.task_list

    def shortSummary(self):
        return f"StopWatch '{self.getId()}': running time = {self.getTotalTimeNanos()} ns"

    def prettyPrint(self):
        summary = self.shortSummary()
        result = [summary]
        if not self.keep_task_list:
            result.append("No task info kept")
        else:
            result.append("---------------------------------------------")
            result.append("ns         %     Task name")
            result.append("---------------------------------------------")
            for task in self.getTaskInfo():
                time_nanos = task.getTimeNanos()
                time_percent = time_nanos / self.getTotalTimeNanos()
                result.append(f"{time_nanos:>9}  {time_percent:>7.3%}  {task.getTaskName()}")
        return "\n".join(result)

    def __str__(self):
        summary = self.shortSummary()
        if self.keep_task_list:
            task_info_str = "; ".join([f"[{task.getTaskName()}] took {task.getTimeNanos()} ns = {task.getTimeNanos() / self.getTotalTimeNanos():.0%}" for task in self.getTaskInfo()])
            return summary + "; " + task_info_str
        return summary + "; no task info kept"


class TaskInfo:
    def __init__(self, task_name, time_nanos):
        self.task_name = task_name
        self.time_nanos = time_nanos

    def getTaskName(self):
        return self.task_name

    def getTimeNanos(self):
        return self.time_nanos

    def getTimeMillis(self):
        return self.time_nanos // 1_000_000

    def getTimeSeconds(self):
        return self.time_nanos / 1_000_000_000

if __name__ == '__main__':
    # 创建一个 StopWatch 对象
    stopwatch = StopWatch("MyStopWatch")

    # 开始一个任务
    stopwatch.start("Task 1")
    time.sleep(1)  # 模拟任务执行
    stopwatch.stop()

    # 开始另一个任务
    stopwatch.start("Task 2")
    time.sleep(2)  # 模拟任务执行
    stopwatch.stop()

    # 打印简洁摘要
    print(stopwatch.shortSummary())

    # 打印详细信息
    print(stopwatch.prettyPrint())