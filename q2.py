class Node:
    def _init_(self, key, color):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color  # 'R' for red, 'B' for black

class RedBlackTree:
    def _init_(self):
        self.nil = Node(None, 'B')  # Nil leaf node
        self.root = self.nil

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        z = Node(key, 'R')
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z.parent.color == 'R':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'R':
                    z.parent.color = 'B'
                    y.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'R':
                    z.parent.color = 'B'
                    y.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'B'

    def delete(self, key):
        z = self._search(key)
        if z == self.nil:
            return
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'B':
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        while x != self.root and x.color == 'B':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'B' and w.right.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.right.color == 'B':
                        w.left.color = 'B'
                        w.color = 'R'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.right.color = 'B'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'B' and w.left.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.left.color == 'B':
                        w.right.color = 'B'
                        w.color = 'R'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.left.color = 'B'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'B'

    def _transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def _search(self, key):
        x = self.root
        while x != self.nil:
            if key == x.key:
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return self.nil