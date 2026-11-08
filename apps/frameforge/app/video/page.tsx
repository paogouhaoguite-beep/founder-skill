import { Suspense } from "react";
import Studio from "@/components/Studio";

export const metadata = { title: "Video studio · Frameforge" };

export default function VideoPage() {
  return (
    <Suspense>
      <Studio mode="video" />
    </Suspense>
  );
}
