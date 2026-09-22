class Solution:
    def resultArray(
        self,
        nums: list[int],
        k: int,
        queries: list[list[int]]
    ) -> list[int]:

        n = len(nums)

        # tree[node] = (product_mod_k, prefix_count)
        tree = [None] * (4 * n)

        def make_leaf(value):
            r = value % k
            cnt = [0] * k
            cnt[r] = 1
            return (r, cnt)

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            left_prod, left_cnt = left
            right_prod, right_cnt = right

            prod = (left_prod * right_prod) % k

            # Prefixes completely inside left
            cnt = left_cnt[:]

            # Prefixes containing all of left
            # + some prefix of right
            for r in range(k):
                new_r = (left_prod * r) % k
                cnt[new_r] += right_cnt[r]

            return (prod, cnt)

        def build(node, l, r):
            if l == r:
                tree[node] = make_leaf(nums[l])
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, value):
            if l == r:
                tree[node] = make_leaf(value)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return None

            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            left = query(
                node * 2,
                l,
                mid,
                ql,
                qr
            )

            right = query(
                node * 2 + 1,
                mid + 1,
                r,
                ql,
                qr
            )

            # Order matters!
            return merge(left, right)

        build(1, 0, n - 1)

        result = []

        for index, value, start, x in queries:

            nums[index] = value

            # Persistent update
            update(
                1,
                0,
                n - 1,
                index,
                value
            )

            # Consider nums[start:]
            _, cnt = query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            result.append(cnt[x])

        return result