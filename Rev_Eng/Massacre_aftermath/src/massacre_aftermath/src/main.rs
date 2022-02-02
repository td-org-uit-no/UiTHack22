use std::{io::{self, Write}, thread, time};


static STATIC_SECRET:  [u32;51] = [170, 275, 359, 431, 528, 627, 734, 784, 834, 957, 1023, 1137, 1242, 1352, 1423, 1518, 1634, 1706, 1775, 1870, 1938, 2052, 2163, 2268, 2368, 2463, 2579, 2690, 2785, 2894, 3015, 3110, 3212, 3309, 3425, 3529, 3630, 3744, 3839, 3918, 3996, 4091, 4156, 4264, 4364, 4465, 4579, 4676, 4773, 4883, 5008];

fn encrypt(v: &[u8]) -> Vec<u32> {
    if v.len() == 0 {
        return Vec::new();
    }
    let mut sum : u32 = *v.first().unwrap() as u32;
    let mut res = Vec::with_capacity(v.len());
    
    for c in v {
        let c = *c as u32;
        res.push(sum + (c));
        sum += c;
    }
    
    res
}

fn slow_print(s: &str) {
    for c in s.chars() {
        print!("{}",c);
        io::stdout().lock().flush().unwrap();
        thread::sleep(time::Duration::from_millis(100));
    }
}

fn main() -> io::Result<()> {

    slow_print("Booting console...\n");
    slow_print("Username: admin\n");
    slow_print("Password: ");

    let mut input = String::new();

    loop {
        io::stdin().read_line(&mut input)?;

        if encrypt(input.trim().as_bytes()) == STATIC_SECRET  {
            slow_print("Correct, access granted.");
            break;
        }

        slow_print("Incorrect, try again: ");
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use crate::encrypt;

    fn decrypt(v:Vec<u32> ) -> String {
        let mut prev = v.last().unwrap();
        let mut res = Vec::with_capacity(v.len());
        
        for c in v.iter().rev() {
            if c == prev {
                continue;
            }
            res.push(prev - c);
            prev = c;
        }
        res.push(*v.first().unwrap()/ 2);
        
        String::from_utf8(res.iter().rev().map(|x| *x as u8).collect()).unwrap()
    }

    #[test]
    fn validate_decrypt() {
        let validation_str = "hello world yes this should do the trick";

        let enc = encrypt(validation_str.as_bytes());
        
        assert_eq!(validation_str, decrypt(enc));
    }
}