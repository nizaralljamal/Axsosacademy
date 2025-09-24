from collections import defaultdict

def find_diagonal_order(mat):
    """
    This function takes an m x n matrix and returns its elements in diagonal order.
    """
    # English: If the matrix is empty, return an empty list.
    # عربي: إذا كانت المصفوفة فارغة، قم بإرجاع قائمة فارغة.
    if not mat or not mat[0]:
        return []

    # --- Step 1: Grouping (الخطوة الأولى: التجميع) ---

    # English: Create a dictionary where keys are the sum of coordinates (i+j)
    #          and values are lists of numbers on that diagonal.
    #          defaultdict(list) automatically creates an empty list for new keys.
    # عربي: أنشئ قاموسًا تكون مفاتيحه هي مجموع الإحداثيات (i+j)
    #      وقيمه هي قوائم الأرقام الموجودة على هذا القطر.
    #      defaultdict(list) تقوم تلقائيًا بإنشاء قائمة فارغة للمفاتيح الجديدة.
    groups = defaultdict(list)

    # English: Get the number of rows and columns.
    # عربي: احصل على عدد الصفوف والأعمدة.
    rows = len(mat)
    cols = len(mat[0])

    # English: Loop through each cell of the matrix.
    # عربي: قم بالمرور على كل خلية في المصفوفة.
    for r in range(rows):
        for c in range(cols):
            # English: Calculate the sum of coordinates. This is the diagonal's ID.
            # عربي: احسب مجموع الإحداثيات. هذا هو "معرّف" القطر.
            diagonal_id = r + c
            
            # English: Add the number to its corresponding diagonal group.
            # عربي: أضف الرقم إلى مجموعته القطرية المناسبة.
            groups[diagonal_id].append(mat[r][c])

    # At this point, for mat = [[1,2,3],[4,5,6],[7,8,9]], `groups` will be:
    # {
    #   0: [1],
    #   1: [2, 4],
    #   2: [3, 5, 7],
    #   3: [6, 8],
    #   4: [9]
    # }

    # --- Step 2: Building the Result (الخطوة الثانية: بناء النتيجة) ---

    # English: Create an empty list to store the final result.
    # عربي: أنشئ قائمة فارغة لتخزين النتيجة النهائية.
    result = []

    # English: Loop through the groups, from the first diagonal (key 0) to the last.
    # عربي: قم بالمرور على المجموعات، من القطر الأول (مفتاح 0) إلى الأخير.
    for i in range(len(groups)):
        # English: Get the list of elements for the current diagonal.
        # عربي: احصل على قائمة العناصر للقطر الحالي.
        elements = groups[i]

        # English: If the diagonal ID (i) is EVEN, the path goes UP-RIGHT.
        #          To simulate this, we need to read the elements in REVERSE order.
        # عربي: إذا كان "معرّف" القطر (i) زوجيًا، فإن المسار يتجه لأعلى-يمين.
        #      لمحاكاة ذلك، نحتاج إلى قراءة العناصر بترتيب معكوس.
        if i % 2 == 0:
            result.extend(elements[::-1]) # [::-1] is a trick to reverse a list
        
        # English: If the diagonal ID (i) is ODD, the path goes DOWN-LEFT.
        #          We read the elements in their original order.
        # عربي: إذا كان "معرّف" القطر (i) فرديًا، فإن المسار يتجه لأسفل-يسار.
        #      نقرأ العناصر بترتيبها الأصلي.
        else:
            result.extend(elements)

    # English: Return the final assembled list.
    # عربي: قم بإرجاع القائمة النهائية التي تم تجميعها.
    return result

# --- Example Usage (أمثلة للاستخدام) ---
mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output1 = find_diagonal_order(mat1)
print(f"Input: {mat1}")
print(f"Output: {output1}") # Expected: [1, 2, 4, 7, 5, 3, 6, 8, 9]

print("-" * 20)

mat2 = [[1, 2], [3, 4]]
output2 = find_diagonal_order(mat2)
print(f"Input: {mat2}")
print(f"Output: {output2}") # Expected: [1, 2, 3, 4]