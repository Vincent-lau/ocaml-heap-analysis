open ForwardedRope;;

let r = ref empty;;

for _ = 0 to 4 do
  r := !r ^ of_string "abc"
done;;

let () = Gc.minor ();;

  
let arr = Array.make 6 empty;;

for i = 1 to 5 do
  arr.(i) <- arr.(i-1) ^ of_string "abc"
done;;

let () = 
  Gc.minor ();;
