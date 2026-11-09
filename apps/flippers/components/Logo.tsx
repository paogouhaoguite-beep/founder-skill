/** The Flippers mark: an "F" whose arms are flippers, the lower one mid-flip. */
export default function Logo({ size = 26 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 64 64" aria-hidden="true">
      <defs>
        <linearGradient id="flippers-bg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#ff6a3d" />
          <stop offset="1" stopColor="#ffb36b" />
        </linearGradient>
      </defs>
      <rect width="64" height="64" rx="16" fill="url(#flippers-bg)" />
      <g transform="translate(2.5 1.5)" fill="#fff">
        <rect x="16" y="13" width="10" height="39" rx="5" />
        <path d="M21 13 C31 11.5 42 9 51 11.5 C53.5 12.2 53.8 14.6 52 16.6 C46 23 36 25.5 21 25 Z" />
        <path d="M21 30 C29 29 37 27.5 44 29.5 C46.3 30.2 46.5 32.4 44.8 34.2 C40 39.2 32 41 21 40.5 Z" opacity=".7" />
      </g>
    </svg>
  );
}
