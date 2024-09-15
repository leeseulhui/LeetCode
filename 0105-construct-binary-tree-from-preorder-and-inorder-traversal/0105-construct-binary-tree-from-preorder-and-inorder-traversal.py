# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 인덱스를 빠르게 찾기 위한 딕셔너리 생성
        in_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 내부적으로 재귀적으로 트리를 빌드하는 함수
        def array_to_tree(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # 전위 순회에서 첫 번째 값이 루트
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # 중위 순회에서 루트의 인덱스를 찾음
            in_root = in_map[root_val]
            nums_left = in_root - in_start
            
            # 왼쪽 서브트리 재귀적으로 빌드
            root.left = array_to_tree(pre_start + 1, pre_start + nums_left, in_start, in_root - 1)
            
            # 오른쪽 서브트리 재귀적으로 빌드
            root.right = array_to_tree(pre_start + nums_left + 1, pre_end, in_root + 1, in_end)
            
            return root
        
        # 전체 범위를 재귀적으로 트리로 변환
        return array_to_tree(0, len(preorder) - 1, 0, len(inorder) - 1)




        