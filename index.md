> A CLI for personal tools


## Installation

```
$ pip install jake
```

## Usage

```
$ jake COMMAND
```

To list commands
```
$ jake --help
```

To get more information about a command
```
$ jake COMMAND --help
```


### Tasks 

> Jake can manage your tasks 

To get more information about tasks
```
$ jake tasks --help
```

Add a new task
```
$ jake tasks add <description>
```

List active tasks
```
$ jake tasks list
```
  * -a list all tasks
  * -c list completed tasks

Mark a task as completed
```
$ jake tasks check <take_id>
```

Unmark a task to make it active
```
$ jake tasks uncheck <take_id>
```

Remove a task
```
$ jake tasks remove <task_id>
```
