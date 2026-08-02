# Payload diagnostic

## Files

### gen14
- `part_000.b64`: 19999 bytes
- `part_001.b64`: 19999 bytes

### remaining
- `part_000.b64`: 19999 bytes
- `part_001.b64`: 19999 bytes
- `part_002.b64`: 19999 bytes
- `part_003.b64`: 19999 bytes
- `part_004a.b64`: 26855 bytes
- `part_004b.b64`: 19830 bytes
- `part_005a.b64`: 16642 bytes

## gen14 attempts

- `joined-base64`: decode error `Error('Incorrect padding')`
- `per-part-base64`: decode error `Error('Incorrect padding')`
- `reverse-joined-base64`: decode error `Error('Incorrect padding')`
- `reverse-per-part-base64`: decode error `Error('Incorrect padding')`

## remaining attempts

- `joined-base64`: decode error `Error('Excess data after padding')`
- `per-part-base64`: decode error `Error('Incorrect padding')`
- `reverse-joined-base64`: decode error `Error('Discontinuous padding not allowed')`
- `reverse-per-part-base64`: decode error `Error('Incorrect padding')`

## Verdict

- gen14 reconstructable: `False`
- remaining reconstructable: `False`
