def counting_sort(arr):
    # Time: O(n + k) where k is the maximum value in arr
    # Space: O(n + k)

    """
    لو محتاج نسخة أفضل ممكن تشوف اصغر قيمة في المصفوفة وتستخدمها لتقليل حجم مصفوفة العد
    مثلا لو المصفوفة فيها أرقام من 50 لـ 100، ممكن
    تستخدم مصفوفة عد بحجم (100 - 50 + 1) = 51
    بدل ما تكون 100
    (هتفيد في بعض الحالات بس الأعم من الواحد)

    ممكن تفكر لو فيه أرقام سالبة تعمل ايه بالظبط (مهم)
    """

    if len(arr) == 0:
        return arr

    n = max(arr) + 1
    count = [0] * n

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(n):
        sorted_arr.extend([i] * count[i])

    return sorted_arr
