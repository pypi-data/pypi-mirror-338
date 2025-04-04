from safe_result import Err, Ok, Result, safe

ok_res = Ok(42)
err_res = Err(ValueError("Bad data"))

print(ok_res.unwrap())  # -> 42
# err_res.unwrap()      # -> Raises ValueError: Bad data


@safe
def combined_op(res1: Result[int, Exception], res2: Result[int, Exception]) -> int:
    # unwrap() propagates errors automatically within @safe context
    val1 = res1.unwrap()
    val2 = res2.unwrap()
    return val1 + val2


print(combined_op(Ok(10), Ok(5)))  # -> Ok(15)
print(combined_op(Ok(10), Err(ValueError("Fail"))))  # -> Err(ValueError('Fail'))
