class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        mix = m - 1  # Chỉ số cho nums1, bắt đầu từ phần tử cuối cùng của nums1 có giá trị
        nix = n - 1  # Chỉ số cho nums2, bắt đầu từ phần tử cuối cùng
        right = m + n - 1  # Chỉ số cho vị trí cần đặt giá trị trong nums1

        while nix >= 0:
            if mix >= 0 and nums1[mix] > nums2[nix]:
                nums1[right] = nums1[mix]  # Đặt giá trị lớn hơn vào cuối nums1
                mix -= 1
            else:
                nums1[right] = nums2[nix]  # Đặt giá trị từ nums2 vào cuối nums1
                nix -= 1
            right -= 1

# Sử dụng
a = Solution()  # Khởi tạo đối tượng Solution
nums1 = [1, 2, 3, 0, 0, 0]  # nums1 có 3 phần tử hợp lệ và 3 ô trống
m = 3
nums2 = [2, 5, 6]  # nums2 có 3 phần tử
n = 3

a.merge(nums1, m, nums2, n)
print(nums1)

