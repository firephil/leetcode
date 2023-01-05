
case class ListNode(_x: Int = 0, _next: ListNode = null) {
   var next: ListNode = _next
   var x: Int = _x
   def foreach(f: Int => Unit): Unit = {
      f(x)
      if (next != null) next.foreach(f)
   }
}

def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
   var carry = 0
   var head = new ListNode()
   var tail = head
   var p = l1
   var q = l2
   while (p != null || q != null) {
      val x = if (p != null) p.x else 0
      val y = if (q != null) q.x else 0
      val sum = carry + x + y
      carry = sum / 10
      tail.next = new ListNode(sum % 10)
      tail = tail.next
      if (p != null) p = p.next
      if (q != null) q = q.next

        if (carry > 0){
            tail.next = new ListNode(carry)
        }
   }
   head.next
}


def add2Numbers(l1: ListNode, l2: ListNode): ListNode = {
   var carry = 0
   var head = new ListNode()
   var tail = head
   var p = l1
   var q = l2
   
   while (p != null || q != null) {
      val x = if (p != null) p.x else 0
      val y = if (q != null) q.x else 0
      var sum = carry + x + y
      
      if (sum > 9) {
        carry = 1
        sum = sum - 10
      }
      else 
        carry = 0

      tail.next = new ListNode(sum)
      tail = tail.next
      if (p != null) p = p.next
      if (q != null) q = q.next

        if (carry > 0){
            tail.next = new ListNode(carry)
        }
   }
   head.next
}

// Recursive solution using optionals and patter matching
def addTwoNumbersOptionals(l1: ListNode, l2: ListNode): ListNode = {

    def addTwoNumbers_(n1: ListNode, n2: ListNode, carry: Int): ListNode = {
        (Option(n1), Option(n2)) match {
            case (Some(num1), Some(num2)) =>

                val sum = num1.x + num2.x + carry
                val rem = sum % 10
                val newCarry = sum / 10

                new ListNode(rem, addTwoNumbers_(num1.next, num2.next, newCarry))

            case (Some(num), None) =>

                val sum = num.x + carry
                val rem = sum % 10
                val newCarry = sum / 10

                new ListNode(rem, addTwoNumbers_(num.next, null, newCarry))

            case (None, Some(num)) =>

                val sum = num.x + carry
                val rem = sum % 10
                val newCarry = sum / 10

                new ListNode(rem, addTwoNumbers_(null, num.next, newCarry))

            case (None, None) =>
                if(carry != 0) new ListNode(carry) else null
        }
    }
    addTwoNumbers_(l1, l2, 0)
    }

@main 
def hello() = 
    val l1 = ListNode(2, ListNode(4, ListNode(3)))
    val l2 = ListNode(5, ListNode(6, ListNode(4)))
    val res = addTwoNumbersOptionals (l1,l2)
    res.foreach(print)