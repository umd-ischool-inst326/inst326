from memobox import Memobox

gc = Memobox("Ground Control")
mt = Memobox("Major Tom")

gc.add_contact(mt)
mt.add_contact(gc)

gc.send_memo("Major Tom", "Take your protein pills and put your helmet on")
gc.send_memo("Major Tom", "Commencing countdown, engines on")

mt.read_memos()

mt.send_memo("Ground Control", "I'm stepping through the door")
mt.send_memo("Ground Control", "I'm floating in a most peculiar way")

gc.read_memos()

mt.read_memos()
