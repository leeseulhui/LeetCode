# 트리 노드 클래스 정의
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 클래스 정의
class Solution:
    def __init__(self):
        self.ans = float('-inf')  # 최댓값을 저장할 변수
    
    def oneSideMax(self, root):
        if root is None:
            return 0
        
        # 왼쪽과 오른쪽에서의 최대 경로를 계산
        left = max(0, self.oneSideMax(root.left))
        right = max(0, self.oneSideMax(root.right))
        
        # 현재 노드를 루트로 하는 경로의 최대값을 갱신
        self.ans = max(self.ans, left + right + root.val)
        
        # 한쪽 서브트리로만 연결된 경로 중 최대값을 반환
        return max(left, right) + root.val
    
    def maxPathSum(self, root):
        self.oneSideMax(root)
        return self.ans

# 예시 트리 생성 및 실행
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

# Solution 객체 생성 후 maxPathSum 호출
solution = Solution()
result = solution.maxPathSum(root)
print(result)
