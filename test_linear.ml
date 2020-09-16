open ForwardedRope;;

let r = ref empty;;

for _ = 1 to 10 do
  r := !r ^ of_string "abc"
done;;

let () = 
  Gc.minor ();;

let arr = Array.make 10 empty;;

for i = 1 to 9 do
  arr.(i) <- arr.(i-1) ^ of_string "abc"
done;;

let () = 
  Gc.minor ();;
