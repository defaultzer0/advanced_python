# CircularBuffer
1. Описание класса присутствует в файле CircularBuffer.py
2. Отсутствуют асинхронные вызовы, потому что не нужны (могу добавить mutex-ы, но смысла в этом нет)
3. Вместо yield присутствует переопределение magic-метода __ iter __
