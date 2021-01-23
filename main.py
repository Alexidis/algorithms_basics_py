import main
import pkgutil

if __name__ == '__main__':
    (lesson_num, task_num) = input('Введите номер урока и номер задания через пробел ').split(' ')
    lesson_name = f'l{lesson_num}'
    task_name = f'task{task_num}'
    task_nums_list = []
    try:
        lesson = getattr(main, lesson_name)
        task_nums_list = [modname[8:] for importer, modname, ispkg in pkgutil.iter_modules(lesson.__path__)]
        task = getattr(lesson, task_name)
    except AttributeError:

        if task_nums_list:
            raise NotImplementedError(f'В уроке {lesson_num} нет задания {task_num} \n'
                                      f' Список номер заданий в уроке {task_nums_list}')
        else:
            raise NotImplementedError(f'Урока с номером {lesson_num} не существует')
    task()
описание